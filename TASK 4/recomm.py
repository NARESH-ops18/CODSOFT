

import math
ratings = {
    "Alice": {
        "The Matrix": 5,
        "John Wick": 4,
        "Inception": 5,
        "The Notebook": 1
    },
    "Bob": {
        "The Matrix": 5,
        "John Wick": 5,
        "Inception": 4
    },
    "Charlie": {
        "The Matrix": 4,
        "Interstellar": 5,
        "The Notebook": 2
    },
    "Diana": {
        "John Wick": 5,
        "Inception": 4,
        "Interstellar": 4,
        "The Notebook": 1
    },
    "Eve": {
        "The Matrix": 2,
        "Interstellar": 5,
        "The Notebook": 4
    }
}

def pearson_correlation(user1, user2):
    # Movies rated by both users
    common = set(ratings[user1].keys()) & set(ratings[user2].keys())
    n = len(common)
    if n == 0:
        return 0  # no overlap

    # Sums and sums of squares
    sum1 = sum(ratings[user1][m] for m in common)
    sum2 = sum(ratings[user2][m] for m in common)

    sum1_sq = sum(ratings[user1][m] ** 2 for m in common)
    sum2_sq = sum(ratings[user2][m] ** 2 for m in common)

    # Sum of products
    prod_sum = sum(ratings[user1][m] * ratings[user2][m] for m in common)

    # Pearson formula
    num = prod_sum - (sum1 * sum2 / n)
    den = math.sqrt((sum1_sq - (sum1 ** 2) / n) * (sum2_sq - (sum2 ** 2) / n))
    if den == 0:
        return 0
    return num / den

# ---------------------------------------------------
# 3. Get top similar users for a target user
# ---------------------------------------------------
def top_similar_users(target_user, n=3):
    scores = []
    for other in ratings:
        if other == target_user:
            continue
        sim = pearson_correlation(target_user, other)
        scores.append((sim, other))
    # sort by similarity (high to low)
    scores.sort(reverse=True, key=lambda x: x[0])
    return scores[:n]

# ---------------------------------------------------
# 4. Recommend movies for a user
# ---------------------------------------------------
def recommend_movies_for_user(target_user, n_recommendations=3):
    totals = {}     # weighted sum of ratings
    sim_sums = {}   # sum of similarities

    for other in ratings:
        if other == target_user:
            continue
        sim = pearson_correlation(target_user, other)
        if sim <= 0:
            continue  # ignore negative or zero similarity

        for movie, rating in ratings[other].items():
            # Only consider movies the target user has not rated
            if movie not in ratings[target_user]:
                # Weighted sum of rating times similarity
                totals.setdefault(movie, 0)
                totals[movie] += rating * sim

                # Sum of similarities
                sim_sums.setdefault(movie, 0)
                sim_sums[movie] += sim

    # Build the normalized score list (weighted average)
    rankings = []
    for movie in totals:
        score = totals[movie] / sim_sums[movie]
        rankings.append((score, movie))

    # Sort: highest score first
    rankings.sort(reverse=True, key=lambda x: x[0])

    # Return movie titles only
    return [movie for score, movie in rankings[:n_recommendations]]

# ---------------------------------------------------
# 5. Simple CLI
# ---------------------------------------------------
def main():
    print("Users in the system:")
    for user in ratings.keys():
        print(" -", user)

    target_user = input("\nEnter user name exactly as shown: ").strip()

    if target_user not in ratings:
        print("User not found!")
        return

    print("\nMovies already rated by", target_user + ":")
    for movie, rating in ratings[target_user].items():
        print(f" - {movie}: {rating}")

    recs = recommend_movies_for_user(target_user, n_recommendations=3)

    if not recs:
        print("\nNo new movie recommendations could be generated.")
    else:
        print("\nRecommended movies for", target_user + ":")
        for m in recs:
            print(" -", m)

if __name__ == "__main__":
    main()
