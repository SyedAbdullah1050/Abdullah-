import speech_recognition as sr
import pyttsx3

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return recognize_speech()

    return query.lower()

def process_query(query):
    if "hello" in query:
        text_to_speech("Hello! How can I help you?")
    elif "what is your name" in query:
        text_to_speech("I am your Jarvis assistant.")
    elif "how are you" in query:
        text_to_speech("I am doing great, thank you!")
    elif "bye" in query:
        text_to_speech("Goodbye!")
        exit()
    else:
        text_to_speech("I don't understand your query. Please try again.")

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        query = recognize_speech()
        process_query(query)