from scraper import Scraper
from settings import LOCATIONS, TIMERANGE, DAY_PERIOD, NIGHT_PERIOD, EARLESTDAY, APPT_TYPE, REAPPT, HEARTBEAT_PERIOD
from bot import Bot
from logger import Logger
from datetime import datetime, timedelta
import time
import threading


class App:
    def __init__(self):
        self.logger = Logger()
        self.bot = Bot()
        self.scraper = Scraper(APPT_TYPE, EARLESTDAY, TIMERANGE, REAPPT, True)

    def run(self):
        self.logger.log("App start")
        self.bot.post_text("Bot starts working!")
        heartbeat = datetime.now()

        while True:
            if (datetime.now() - heartbeat) / timedelta(minutes=HEARTBEAT_PERIOD) > 1:
                self.bot.post_text("Still working...")
                heartbeat = datetime.now()

            if not self._is_daytime():
                self.logger.log("Is nightime, start a new round")
                self.run_once()
                self.logger.log("End a round")
                time.sleep(NIGHT_PERIOD)
            else:
                self.logger.log("Is daytime, start a new round")
                self.run_once()
                self.logger.log("End a round")
                time.sleep(DAY_PERIOD)

    def run_once(self):
        for location, office_id in LOCATIONS.items():
            appt, valid, complete = self.scraper.i_want_an_appointment_at(office_id)
            if valid:
                msg = "*{}*\n{}".format(location, appt)
                self.bot.post_message(msg)

                if complete:
                    self.logger.log("Appointment at %s has been made, finish." % appt)
                    self.bot.post_text("Appointment has been made :)")
                    exit(0)
            else:
                self.logger.log("No required available date.")

    def _is_daytime(self):
        curr_hour = datetime.now().hour
        return True if not 1 <= curr_hour <= 7 else False

    def _sleep_till_morning(self):
        self.logger.log("Is night time, going to sleep now.")
        sleep_in_hours = 7 - datetime.now().hour
        time.sleep(sleep_in_hours * 3600)


if __name__ == "__main__":
    app = App()
    app.run()
