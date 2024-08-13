from text_to_speech import TextToSpeech

class ScheduleCheckup:
    def __init__(self):
        self.text_to_speech = TextToSpeech()

    def schedule_checkup(self):
        self.text_to_speech.speak("Scheduling a regular checkup.")
        # Logic to schedule a checkup
