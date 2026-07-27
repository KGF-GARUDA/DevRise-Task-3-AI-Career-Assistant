from chatbot import AIChatbot

bot = AIChatbot()

print("=" * 50)
print("🤖 AI Career Assistant")
print("Type 'exit' to quit")
print("=" * 50)

while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        print("\nBot: Goodbye! 👋")
        break

    answer = bot.chat(user)

    print("\nBot:\n")
    print(answer)