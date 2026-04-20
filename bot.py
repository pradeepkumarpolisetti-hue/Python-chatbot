def chatbot():
    print("Bot: Hi! I'm a chatbot. Type 'exit' to stop.")
    while True:
        user = input("You: ").lower()
        if user == "exit":
            print("Bot: Goodbye!")
            break
        elif user in ["hi", "hello"]:
            print("Bot: Hello! Nice to meet you.")
            name = input("Bot: What's your name? ")
            print("Bot: Nice name, " + name + "!")
        elif user in ["thank you", "tq","tqs"]:
            print("Bot: You're welcome!", name)
        elif "ai" in user:
            print("Bot: AI stands for Artificial Intelligence")
        elif user in ["you are too good", "you are nice"]:
            print("Bot:Awee, You make me feel shy.")
            print("    Just kidding.")
        else:
            print("Bot: I didn't understand that yet, but I'm learning new things!")
chatbot()