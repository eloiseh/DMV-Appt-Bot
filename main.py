from scraper import Scraper
from settings import LOCATIONS, TIMERANGE, PERIOD, EARLESTDAY
from bot import Bot
from database import DB
from logger import Logger
from datetime import datetime
from datetime import timedelta
import time
import threading

class App:
    def __init__(self):
        self.db = DB()
        self.logger = Logger()
        self.bot = Bot()
        self.scraper = Scraper()

    def run(self):
        self.logger.log("App start")

        while True:
            if not self._is_daytime():
                self.logger.log("Is night, going to sleep")
                self._sleep_till_morning()
                self.logger.log("Waking up from sleep")
            else:
                self.logger.log("Is daytime, start a new round")
                self.run_once()
                self.logger.log("End a round")
                time.sleep(PERIOD)

    def run_once(self):
        for location, office_id in LOCATIONS.items():
            # self.logger.log("Checking appointment for %s" % location)
            appt = self.scraper.i_want_an_appointment_at(office_id)
            if appt:
                # self.logger.log("Appointment retrieved from web page")
                if self._check_time_require(appt):
                    if not self.db.appt_exists(location, appt):
                        self.logger.log("New appointment found. Added to DB.")
                        msg = "*{}*\n{}".format(location, appt)
                        self.bot.post_message(msg)
                    else:
                        self.logger.log("Appointment already exists in DB.")
                else:
                    self.logger.log("Date doesn't meet requirement.")
            else:
                self.logger.log("Invalid appointment object returned")

    def _check_time_require(self, timestr):
        time_dmv = datetime.strptime(timestr.strip(), '%A, %B %d, %Y at %I:%M %p')
        time_now = datetime.strptime(EARLESTDAY, '%B %d, %Y')
        diff = (time_dmv - time_now)/timedelta(days=1)
        return diff < TIMERANGE

    def _is_daytime(self):
        curr_hour = datetime.now().hour
        # return True if not 0 <= curr_hour <= 8 else False
        return True

    def _sleep_till_morning(self):
        self.logger.log("Is night time, going to sleep now.")
        sleep_in_hours = 8 - datetime.now().hour
        time.sleep(sleep_in_hours * 3600)

if __name__ == "__main__":
    app = App()
    app.run()
