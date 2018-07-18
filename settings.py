SLACK_CHANNEL = 'bot'  # the slack channel which you want to send messages to
APPT_TYPE = 2  # 1 for general appointment(writen test, renew, replace license), 2 for driving test
REAPPT = True  # True for rescheduling an appointment, False for first-time appointment
DRIVE_URL = 'https://www.dmv.ca.gov/wasapp/foa/clear.do?goTo=driveTest'  # driving test url
WRITEN_URL = 'https://www.dmv.ca.gov/wasapp/foa/clear.do?goTo=officeVisit&localeName=en'  # writen test url
TIMERANGE = 21  # maximum days from earliest day
EARLESTDAY = "July 18, 2018"  # desired earliest desired day
START_HOUR = 8  # desired earliest hour
END_HOUR = 16  # desired latest hour
DAY_PERIOD = 20  # num of seconds period for each query round at daytime
NIGHT_PERIOD = 150  # num of seconds period for each query round at nighttime
NOTIFICATION_TYPE = 1  # 1 for email, 2 for sms. notification actually doesn't work in dmv system
HEARTBEAT_PERIOD = 60  # num of minutes period for heartbeat message sent to slack
LOCATIONS = {  # the office ID obtained by inspecting the xpath
    'Redwood City': '548',
    'San Jose': '516',
    'Santa Clara': '632',
    'Las Gatos': '640',
}
PROFILE = {  # Your information
    'first_name': 'Winnie',
    'last_name': 'Xi',
    'tel_prefix': 'xxx',
    'tel_suffix1': 'xxx',
    'tel_suffix2': 'xxxx',
    'email': 'xxxx@gmail.com',
    ##### Following only required for driving test #####
    'mm': 'xx',
    'dd': 'xx',
    'yyyy': 'xxxx',
    'dl_number': 'XXXXXX'
}
