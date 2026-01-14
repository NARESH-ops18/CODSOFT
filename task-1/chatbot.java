import java.util.Scanner;

public class Chatbot {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("🤖 ChatBot: Hello! I'm your simple rule-based chatbot.");
        System.out.println("Type 'exit' to end the chat.\n");

        while (true) {
            System.out.print("You: ");
            String input = scanner.nextLine().toLowerCase();

            if (input.equals("exit")) {
                System.out.println("🤖 ChatBot: Goodbye! Take care.");
                break;
            } else if (input.contains("hello") || input.contains("hi")) {
                System.out.println("🤖 ChatBot: Hi there! How can I assist you today?");
            } else if (input.contains("how are you")) {
                System.out.println("🤖 ChatBot: I'm just code, but I'm doing great! 😄");
            } else if (input.contains("your name")) {
                System.out.println("🤖 ChatBot: I'm CodSoftBot, your Java assistant.");
            } else if (input.contains("bye")) {
                System.out.println("🤖 ChatBot: Bye! Have a great day.");
            } else {
                System.out.println("🤖 ChatBot: Sorry, I didn't quite catch that.");
            }
        }

        scanner.close();
    }
}