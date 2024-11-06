import re
responses = {
    "hello": "Hello, movie buff! What's on your mind today?",
    "price": "Could you tell me which movie ticket or merchandise you're interested in?",
    "information": "We're Cinema Galaxy, your go-to place for all things movies and entertainment.",
    "name": "Our theater is Cinema Galaxy, where every seat is the best seat in the house!",
    "hours": "Our showtimes run from Monday to Sunday, 10AM to Midnight.",
    "address": "We’re located at 134 Film Street, Springfield. Come visit us for the ultimate movie experience!",
    "contact": "Feel free to reach out at contact@cinemagalaxy.com or call us at (555) 123-4688.",
    "help": "I'm here to assist with your movie needs. Ask me anything about our screenings, tickets, or theater services!",
    "default": "Hmm, I'm not quite sure about that. Could you give me more details about your movie-related question?",
    "interstellar" : "RS. 550"
}

def get_response(message):
    message = message.lower()

    for key in responses:
        if re.search(r'\b' + re.escape(key) + r'\b', message):
            return responses[key]
        
    return responses["default"]
    
def chatbot():
    print("Welcome to Cinema Galaxy's chatbot! Ask me anything about our theater. Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("ChatBot: Goodbye! Enjoy your next movie!")
            break
        response = get_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chatbot()
