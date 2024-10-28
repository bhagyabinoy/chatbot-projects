import openai
from nltk.chat.util import Chat, reflections


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hi there!", "Greetings!",]
    ],
    [
        r"how are you?",
        ["I'm just a program, but thanks for asking!", "Doing well, how about you?",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot.",]
    ],
    [
        r"quit",
        ["Bye! Take care!", "See you later!",]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that.",]
    ],
]


def get_openai_response(prompt):
    try:
      openai.api_key = ''  # Replace with your actual OpenAI API key
      response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo", 
          messages=[
              {"role": "user", "content": prompt}
          ]
      )
      return response['choices'][0]['message']['content']
    except Exception as e:
        print(e,"---exception")
        response == "I'm sorry, I don't understand that."
        return response

# Create the chatbot
chatbot = Chat(pairs, reflections)

def chat_with_bot():
    print("Hi! I'm a chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Bye! Take care!")
            break
        
        response = chatbot.respond(user_input)
        if response == "I'm sorry, I don't understand that.":
            response = get_openai_response(user_input)
        
        print("Chatbot:", response)

chat_with_bot()