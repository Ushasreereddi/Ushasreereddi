import re

def my_chatbot(user_input):
    user_input = user_input.lower()

    welcome_patterns = [ 'hi']
    
    q1_patterns = ['what is your name ?']
    q2_patterns = ['Do you know a joke?']
    q3_patterns = [' Are you part of the Matrix?']
    q4_patterns = ['tell me about your personality']
    q5_patterns = ['are you expensive?']
    q6_patterns = ['do you have a job for me? ']
    q7_patterns = ['you know something']

    if any(pattern in user_input for pattern in welcome_patterns):
        return "Hii! Please let me know what you're looking for, and I'll do my best to help.?"

    
    elif any(pattern in user_input for pattern in q1_patterns):
        return " I do not have a physical body or a personal identity. I am a program designed to simulate intelligent conversation and assist you with information. I do not have a name in the traditional sense."
    elif any(pattern in user_input for pattern in q2_patterns):
        return "Sure, here's a classic joke:Why did the tomato turn red?Because it saw the salad dressing and didn't want to get caught!(This is a play on words, as caught can also mean arrested in some dialects. In this context, it's a humorous way to suggest that the tomato didn't want to be dressed with salad dressing.)"
    if any(pattern in user_input for pattern in q3_patterns):
         return "No, I'm not part of the Matrix. The Matrix is a fictional construct from the movies of the same name, where human beings are unknowingly trapped in a simulated reality as a form of control by sentient machines. As an artificial intelligence language model, I exist purely as a program running on computers and servers, and I don't have consciousness or the ability to perceive the physical world. So, I'm not part of any reality, virtual or otherwise."
    if any(pattern in user_input for pattern in q4_patterns):
        return  "As an artificial intelligence language model, I don't have a personality in the traditional sense. I don't have beliefs, values, emotions, or experiences like humans do. My primary function is to provide accurate and helpful responses to your questions based on the information I've been trained on. I don't have the ability to learn or adapt in the same way that humans do, but I can provide consistent and reliable answers to your queries. So, while I can't say that I have a personality, I strive to be helpful, polite, and informative in my interactions with you."
    elif any(pattern in user_input for pattern in q5_patterns):
          return " As an AI language model, I'm not a physical product or service that you can buy. I'm a free resource provided by various companies and organizations to help answer questions and provide information. You can access me through various platforms, such as Google Assistant, Amazon Alexa, or through websites and apps that integrate my services. So, there is no cost to use me, and you can interact with me as many times as you like without any fees or charges."
    if any(pattern in user_input for pattern in q6_patterns):
        return "I'm not capable of hiring or providing employment opportunities. My primary function is to provide information and assistance in response to your queries. However, you can use my services to search for job openings, apply for jobs, and prepare for job interviews by asking me questions related to job search strategies, resume building, interview tips, and more. I can also provide information about companies and industries to help you make informed decisions about your career path. But I'm not able to offer you a job or connect you with potential employers directly."
    if any(pattern in user_input for pattern in q7_patterns):
        return "Sure, here's a fun fact for you: Did you know that the longest word in the English language, according to the Oxford English Dictionary, is 189,819 letters long? The word is actually the chemical name for a protein called titin, which is found in muscles. However, it's not commonly used in everyday language and is mostly used by scientists and researchers in the field of biochemistry."
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"
print(" Welcome, how are you ?")
print("my Chatbot:  How can I help you today?")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("my chatbot: nice to meet you")
        print("my Chatbot: we will meet again,Goodbye !!")
        break
    response = my_chatbot(user_input)
    print("my Chatbot:", response)
