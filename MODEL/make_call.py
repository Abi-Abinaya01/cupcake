import re
from text_to_speech import TextToSpeech

class MakeCall:
    def __init__(self):
        self.text_to_speech = TextToSpeech()

    def make_call(self, text):
        phone_number = self.extract_phone_number(text)
        if phone_number:
            self.text_to_speech.speak(f"Calling {phone_number}.")
            # Logic to make a call
        else:
            self.text_to_speech.speak("I couldn't find a phone number in your request.")

    def extract_phone_number(self, text):
        match = re.search(r'\b\d{10}\b', text)
        return match.group(0) if match else None
