# simple_chatgpt.py

def get_response(user_input):
    """
    Generate a simple AI-like response based on keywords in user_input.
    """
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "name" in user_input:
        return "I am a simple ChatGPT-like bot built in Python."
    elif "help" in user_input:
        return "Sure, I can help. Please tell me your query."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that yet. I'm still learning."

def start_chat():
    """
    Start a basic chatbot interaction loop.
    """
    print("🤖 ChatGPT Simulator: Type 'bye' to end the chat.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)
        if user_input.lower() == "bye":
            break
