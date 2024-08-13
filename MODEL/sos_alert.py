from text_to_speech import TextToSpeech

class SOSAlert:
    def __init__(self):
        self.text_to_speech = TextToSpeech()

    def trigger_sos_alert(self):
        self.text_to_speech.speak("Triggering SOS alert.")
        self.sos_call()
        self.notification_system()

    def sos_call(self):
        self.text_to_speech.speak("Placing SOS call to the nearest hospital.")
        # Logic to place an SOS call

    def notification_system(self):
        self.text_to_speech.speak("Sending notifications to caretaker, relatives, and consulting doctors.")
        # Logic to send notifications
