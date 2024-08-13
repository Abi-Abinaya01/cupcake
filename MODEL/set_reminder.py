import re
import schedule
import time
from text_to_speech import TextToSpeech

class SetReminder:
    def __init__(self):
        self.text_to_speech = TextToSpeech()

    def set_reminder(self, text):
        reminder_text = self.extract_reminder_text(text)
        reminder_time = self.extract_reminder_time(text)

        if reminder_text and reminder_time:
            self.text_to_speech.speak(f"Setting a reminder for {reminder_text} at {reminder_time}.")
            self.schedule_notification(reminder_text, reminder_time)
        else:
            self.text_to_speech.speak("I couldn't set the reminder. Please provide a valid time and reminder text.")

    def extract_reminder_text(self, text):
        return text.replace(re.findall(r'\b\d{1,2}:\d{2}\b', text)[0], '').strip()

    def extract_reminder_time(self, text):
        match = re.search(r'\b\d{1,2}:\d{2}\b', text)
        return match.group(0) if match else None

    def schedule_notification(self, reminder_text, reminder_time):
        hour, minute = map(int, reminder_time.split(':'))
        schedule.every().day.at(f"{hour}:{minute}").do(self.notify, reminder_text)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def notify(self, reminder_text):
        self.text_to_speech.speak(f"Reminder: {reminder_text}")
