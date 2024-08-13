from speech_recognizer import SpeechRecognizer
from text_to_speech import TextToSpeech
from intent_processor import IntentProcessor

def main():
    speech_recognizer = SpeechRecognizer()
    text_to_speech = TextToSpeech()
    intent_processor = IntentProcessor()

    text_to_speech.speak("Welcome to the voice assistance system. How can I help you?")

    while True:
        text = speech_recognizer.recognize_speech()
        if text:
            intent_processor.process_intent(text)

if __name__ == "__main__":
    main()