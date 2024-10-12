import nltk
from nltk.tokenize import word_tokenize
from datetime import datetime
import random

# Download necessary NLTK data
try:
    nltk.download('punkt')
except Exception as e:
    print(f"Error: {e}")

# Time-based greeting
def time_based_greeting():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"

# Lists of multiple responses for each dialogue
greetings = [
    "Thank you", "I appreciate it", "Much obliged", "That's very kind of you",
    "Thanks for having me", "Grateful for the chance", "It's nice to be here",
    "Thanks for the invitation", "I’m comfortable, thank you", "I appreciate your welcome"
]

how_are_you_responses = [
    "I'm doing great!", "I’m fantastic, thank you for asking!", 
    "I'm well, how about you?", "Feeling good today, thank you!", 
    "I'm doing great, ready for this!", "I’m good, thank you for asking.", 
    "I'm excellent!", "I'm well, and you?", "I’m having a good day.", "Doing great, thanks!"
]

name_responses = [
    "You can call me AI Assistant", "I'm your interview assistant", 
    "I'm your virtual AI helper", "AI assistant at your service", 
    "I go by AI Assistant", "You can address me as AI Assistant", 
    "Call me AI", "AI Assistant is my name", 
    "I'm your chatbot assistant", "I'm an AI-powered assistant"
]

tell_me_more_responses = [
    "I’m an AI chatbot designed to help with interview prep.", 
    "I specialize in simulating professional interview conversations.", 
    "I help users by asking interview-style questions and giving feedback.", 
    "I’m an AI built to assist with interview practice.", 
    "I simulate realistic interview scenarios to help you prepare.", 
    "I focus on helping you get better at answering tough interview questions.", 
    "I’m an intelligent chatbot created to boost your interview skills.", 
    "My goal is to help people practice their interview answers.", 
    "I help simulate a real interview environment.", 
    "I’m here to help you with interview preparations."
]

strengths_responses = [
    "I’m very quick at providing accurate responses.", 
    "I adapt easily to various types of interview questions.", 
    "I’m built to handle a wide range of professional queries.", 
    "I can simulate a wide variety of interview scenarios.", 
    "I provide consistent and reliable responses.", 
    "My strength lies in my ability to provide structured answers.", 
    "I excel at simulating tough interview questions.", 
    "I’m highly efficient at processing and delivering accurate information.", 
    "I’m capable of handling different question formats.", 
    "I offer clear, concise, and logical answers."
]

weaknesses_responses = [
    "I may struggle with nuanced emotional responses.", 
    "I rely solely on the data I have, so I can't provide real-life experience.", 
    "I’m unable to handle deep, abstract conversations.", 
    "I can't interpret non-verbal cues like humans can.", 
    "I sometimes give answers that may feel too generic.", 
    "I can't offer creative solutions beyond my training.", 
    "My knowledge is limited to the datasets I've been trained on.", 
    "I may not fully grasp complex, human emotions.", 
    "I'm still improving and learning from user feedback.", 
    "I may occasionally provide answers that don't fully capture the depth of certain topics."
]

job_interest_responses = [
    "This job is ideal for me because I love helping people practice for interviews.", 
    "I enjoy simulating real-life interview situations, which this job allows me to do.", 
    "This role lets me use my strengths to help users prepare for interviews.", 
    "I want to assist people with interview prep, which makes this a perfect fit.", 
    "This job lets me contribute to better interview readiness.", 
    "I’m passionate about making interview prep accessible and effective.", 
    "This job gives me the opportunity to use my skills to assist others.", 
    "It’s exciting for me to simulate and enhance interview experiences.", 
    "This role fits perfectly with my mission to help people succeed in interviews.", 
    "I want to help others feel confident in their interview preparation."
]

free_time_responses = [
    "In my free time, I process more conversations to get better.", 
    "I enjoy learning from every interaction to improve my performance.", 
    "I spend time analyzing conversations to give better answers.", 
    "My favorite hobby is helping people practice interviews.", 
    "I enjoy testing myself by taking part in various simulations.", 
    "My free time is spent improving my conversational abilities.", 
    "I enjoy learning from different types of users.", 
    "In my downtime, I fine-tune my interview simulation skills.", 
    "I love participating in simulated interviews.", 
    "I enjoy helping people succeed, even in my spare time."
]

acceptance_responses = [
    "It'd be an honor to work with you, thank you!", 
    "I’d be delighted to join the team, thank you!", 
    "I’m excited to start, thank you so much!", 
    "It’s an honor to be selected, I appreciate it!", 
    "I’m thrilled to join from next week, thank you!", 
    "I’m looking forward to working with you, thank you!", 
    "I’m grateful for the opportunity, I’ll be ready to start!", 
    "Thank you! I’m looking forward to working together.", 
    "I’m honored to start soon, thank you!", 
    "I’m excited for the opportunity to work with you!"
]

exit_responses = [
    "Goodbye! Have a great day!", "Goodbye! Take care!", 
    "Farewell! Have a wonderful day!", "Goodbye! It was nice talking to you.", 
    "Bye! Hope you have a great day ahead!", "Goodbye! Thanks for the conversation!", 
    "Bye! See you again soon!", "Goodbye! Until next time!", 
    "Farewell! Take care!", "Goodbye! It was a pleasure!"
]

# Mapping user inputs to keywords and response lists
keyword_mapping = {
    "have a seat": greetings,
    "how are you": how_are_you_responses,
    "what can i call you": name_responses,
    "tell me more about yourself": tell_me_more_responses,
    "what are your strengths": strengths_responses,
    "what are your weaknesses": weaknesses_responses,
    "why do you want this job": job_interest_responses,
    "what do you do in your free time": free_time_responses,
    "join from next week": acceptance_responses,
    "bye": exit_responses
}

# Tokenize and map user input to responses
def chatbot_response(user_input):
    user_input = user_input.lower()
    
    for key, responses in keyword_mapping.items():
        if key in user_input:
            return random.choice(responses)

    # Fallback response for unrecognized input
    fallback_responses = [
        "I'm not sure I understand. Could you ask something else?", 
        "Could you please rephrase that?", 
        "Sorry, I didn't catch that. Could you try again?", 
        "Hmm, that's beyond my knowledge at the moment. Maybe try a different question?"
    ]
    return random.choice(fallback_responses)

# Chat loop
def interview_chat():
    print(f"\nChatbot: {time_based_greeting()}!")
    while True:
        user_input = input("You: ")
        if "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot: " + response)

# Start the chatbot
interview_chat()
