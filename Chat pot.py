import nltk
import spacy
from nltk.chat.util import Chat, reflections

# Download required NLTK resources (only once)
nltk.download('punkt')
nltk.download('stopwords')

# Define pattern-response pairs for the chatbot
pairs = [
    (r"hi|hello|hey", ["Hello! How can I help you today?", "Hi there! Need assistance?"]),
    (r"what is your name\??", ["I'm Cod Bot, your virtual assistant."]),
    (r"how are you\??", ["I'm functioning as expected. Thank you!"]),
    (r"what can you do\??", ["I can answer your questions and show you named entities from your messages."]),
    (r"(.*) help (.*)", ["Sure, I'm here to help. Please explain your issue."]),
    (r"bye|quit|exit", ["Goodbye! Have a great day.", "Take care! Ending our chat."]),
    (r"(.*)", ["Sorry, I didn't understand that. Can you rephrase?"])
]

# Initialize the chatbot
chatbot = Chat(pairs, reflections)

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

# Process and respond to user input
def process_input(user_input):
    response = chatbot.respond(user_input)
    entities = [(ent.text, ent.label_) for ent in nlp(user_input).ents]
    return response, entities

# Main function to run the chatbot
def run_chatbot():
    print("CodTech AI Chatbot is online! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "quit", "exit"]:
            print("Bot: Goodbye! Internship completion certificate will be issued on your end date.")
            break
        response, entities = process_input(user_input)
        print("Bot:", response)
        if entities:
            print("Bot (Named Entities):", entities)

# Start chatbot
if __name__ == "__main__":
    run_chatbot()