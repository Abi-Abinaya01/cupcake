from text_to_speech import TextToSpeech
from sos_alert import SOSAlert
from schedule_checkup import ScheduleCheckup
from make_call import MakeCall
from set_reminder import SetReminder

class IntentProcessor:
    def __init__(self):
        self.sos_alert = SOSAlert()
        self.schedule_checkup = ScheduleCheckup()
        self.make_call = MakeCall()
        self.set_reminder = SetReminder()

    def process_intent(self, text):
        if "sos" in text.lower() or "help" in text.lower():
            self.sos_alert.trigger_sos_alert()
        elif "schedule" in text.lower() and "checkup" in text.lower():
            self.schedule_checkup.schedule_checkup()
        elif "call" in text.lower():
            self.make_call.make_call(text)
        elif "reminder" in text.lower():
            self.set_reminder.set_reminder(text)
        else:
            TextToSpeech().speak("I'm sorry, I didn't understand that command.")
