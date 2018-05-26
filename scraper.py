from selenium import webdriver
from settings import PROFILE, DRIVE_URL, WRITEN_URL, APPT_TYPE, NOTIFICATION_TYPE
from logger import Logger
from datetime import datetime, timedelta
from pyvirtualdisplay import Display
import time
import urllib


class Scraper:
    def __init__(self, appt_type, start_date, time_range, auto_make):
        self.logger = Logger()

        self.display = Display(visible=0, size=(1280, 2000))
        self.display.start()

        # Start a real browser or background job 
        # self.browser = webdriver.Chrome('./chromedriver')
        self.browser = webdriver.PhantomJS('phantomjs')
        self.logger.log("New instance of scraper created")
        self.start_date = start_date
        self.time_range = time_range
        self.auto_make = auto_make
        self.type = appt_type

    def i_want_an_appointment_at(self, office_id):
        self.logger.log("Start an appointment searching process for {}.".format(office_id))
        self.browser.delete_all_cookies()
        if APPT_TYPE == 1:
            self.browser.get(WRITEN_URL)
        else:
            self.browser.get(DRIVE_URL)
        time.sleep(3)

        if self.form_fill_and_submit(self.browser, office_id):
            if APPT_TYPE == 1:
                return self.get_permit_appointment(self.browser)
            else:
                return self.get_driving_appointment(self.browser)
        else:
            return None, False, False

    def form_fill_and_submit(self, browser, office_id):
        try:
            browser.find_element_by_xpath('//*[@id="officeId"]/option[@value={}]'.format(office_id)).click()

            if APPT_TYPE == 1:
                browser.find_element_by_xpath('//*[@id="one_task"]').click()
                browser.find_element_by_xpath('//*[@id="taskCID"]').click()
                browser.find_element_by_xpath('//*[@id="first_name"]').send_keys(PROFILE['first_name'])
                browser.find_element_by_xpath('//*[@id="last_name"]').send_keys(PROFILE['last_name'])
                browser.find_element_by_xpath('//*[@id="areaCode"]').send_keys(PROFILE['tel_prefix'])
                browser.find_element_by_xpath('//*[@id="telPrefix"]').send_keys(PROFILE['tel_suffix1'])
                browser.find_element_by_xpath('//*[@id="telSuffix"]').send_keys(PROFILE['tel_suffix2'])
                browser.find_element_by_xpath('//*[@id="app_content"]/form/fieldset/div[8]/input[2]').click()
            elif APPT_TYPE == 2:
                browser.find_element_by_xpath('//*[@id="DT"]').click()
                browser.find_element_by_xpath('//*[@id="first_name"]').send_keys(PROFILE['first_name'])
                browser.find_element_by_xpath('//*[@id="last_name"]').send_keys(PROFILE['last_name'])
                browser.find_element_by_xpath('//*[@id="birthMonth"]').send_keys(PROFILE['mm'])
                browser.find_element_by_xpath('//*[@id="birthDay"]').send_keys(PROFILE['dd'])
                browser.find_element_by_xpath('//*[@id="birthYear"]').send_keys(PROFILE['yyyy'])
                browser.find_element_by_xpath('//*[@id="dl_number"]').send_keys(PROFILE['dl_number'])
                browser.find_element_by_xpath('//*[@id="areaCode"]').send_keys(PROFILE['tel_prefix'])
                browser.find_element_by_xpath('//*[@id="telPrefix"]').send_keys(PROFILE['tel_suffix1'])
                browser.find_element_by_xpath('//*[@id="telSuffix"]').send_keys(PROFILE['tel_suffix2'])
                browser.find_element_by_xpath('//*[@id="app_content"]/form/fieldset/div[5]/input[2]').click()
            
            # self.logger.log("Form filled and submitted for office %s" % office_id)
            browser.switch_to_default_content()
            return True
        except:
            self.logger.log("No valid appointment xpath found when filling 1st form.")
            pass

        return False


    def _check_time_require(self, timestr):
        time_dmv = datetime.strptime(timestr.strip(), '%A, %B %d, %Y at %I:%M %p')
        time_now = datetime.strptime(self.start_date, '%B %d, %Y')
        diff = (time_dmv - time_now)/timedelta(days=1)
        return diff < self.time_range and diff >= 0

    def get_permit_appointment(self, browser):
        time.sleep(3)
        # Found available date
        try:
            element = browser.find_element_by_xpath('//*[@id="app_content"]/form/div[1]/div[2]/table/tbody/tr/td[3]/p[2]/strong').get_attribute('innerHTML')
            if element and element[:5] == 'Sorry':
                return element, False, False
            
            elif self._check_time_require(element):
                print("Find a valid Date!")
                if self.auto_make:
                    browser.find_element_by_xpath('//*[@id="app_content"]/div/a[1]').click()
                    browser.switch_to_default_content()
                    return element, True, self.appt_form_fill(browser)
                else:
                    return element, True, False
            else:
                return element, False, False

        except:
            self.logger.log("No valid appointment xpath found when filling 2nd form.")
            pass

        # No available date
        try:
            element = browser.find_element_by_xpath('//*[@id="app_content"]/table/tbody/tr[2]/td/p').get_attribute('innerHTML')
            self.logger.log("No available appointments")
            return element, False, False
        except:
            self.logger.log("Invalid xpath - no element found")
            pass
        
        return None, False, False

    def get_driving_appointment(self, browser):
        time.sleep(3)
        # Found available date
        try:
            element = browser.find_element_by_xpath('//*[@id="app_content"]/form/div[1]/div[2]/table/tbody/tr/td[2]/p[2]/strong').get_attribute('innerHTML')
            if element and element[:5] == 'Sorry':
                return element, False, False
            
            elif self._check_time_require(element):
                print("Find a valid Date!")
                if self.auto_make:
                    browser.find_element_by_xpath('//*[@id="app_content"]/div/form/input').click()
                    browser.switch_to_default_content()
                    return element, True, self.appt_form_fill(browser)
                else:
                    return element, True, False
            else:
                return element, False, False

        except:
            self.logger.log("No valid appointment xpath found when filling 2nd form.")
            pass

        # No available date
        try:
            element = browser.find_element_by_xpath('//*[@id="app_content"]/table/tbody/tr[2]/td/p').get_attribute('innerHTML')
            self.logger.log("No available appointments")
            return element, False, False
        except:
            self.logger.log("Invalid xpath - no element found")
            pass
        
        return None, False, False

    def appt_form_fill(self, browser):
        time.sleep(3)

        if NOTIFICATION_TYPE == 1:
            browser.find_element_by_xpath('//*[@id="email_method"]').click()
            browser.find_element_by_xpath('//*[@id="notify_email"]').send_keys(PROFILE['email'])
            browser.find_element_by_xpath('//*[@id="notify_email_confirm"]').send_keys(PROFILE['email'])    
        elif NOTIFICATION_TYPE == 2:
            browser.find_element_by_xpath('//*[@id="notify_smsTelArea"]').send_keys(PROFILE['tel_prefix'])
            browser.find_element_by_xpath('//*[@id="notify_smsTelPrefix"]').send_keys(PROFILE['tel_suffix1'])
            browser.find_element_by_xpath('//*[@id="notify_smsTelSuffix"]').send_keys(PROFILE['tel_suffix2'])
            browser.find_element_by_xpath('//*[@id="notify_smsTelArea_confirm"]').send_keys(PROFILE['tel_prefix'])
            browser.find_element_by_xpath('//*[@id="notify_smsTelPrefix_confirm"]').send_keys(PROFILE['tel_suffix1'])
            browser.find_element_by_xpath('//*[@id="notify_smsTelSuffix_confirm"]').send_keys(PROFILE['tel_suffix2'])

        browser.find_element_by_xpath('//*[@id="app_content"]/form/fieldset/div[11]/input[1]').click()
        browser.switch_to_default_content()

        time.sleep(3)
        if APPT_TYPE == 1:
            browser.find_element_by_xpath('//*[@id="app_content"]/form/fieldset/div[10]/input[1]').click()
        elif APPT_TYPE == 2:
            browser.find_element_by_xpath('//*[@id="app_content"]/form/fieldset/div[9]/input[1]').click()
        browser.switch_to_default_content()

        time.sleep(3)
        if "System Unavailable" not in browser.find_element_by_xpath('//*[@id="app_content"]').get_attribute('innerHTML'):
            # save confirmation page in local directory
            browser.save_screenshot("screenshot_%d.png" % int(time.time()))
            time.sleep(2)
            browser.quit()
            self.display.stop()
            return True
        else:
            return False
            





