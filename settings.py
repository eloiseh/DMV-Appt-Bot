SLACK_CHANNEL = 'bot' # this should be the slack channel which you want to send messages to
#URL = 'https://www.dmv.ca.gov/wasapp/foa/findDriveTest.do'  # behind the wheel test
URL = 'https://www.dmv.ca.gov/wasapp/foa/findOfficeVisit.do' # permit test
TIMERANGE = 4
EARLESTDAY = "May 17, 2018"
DAY_PERIOD = 60
NIGHT_PERIOD = 300
LOCATIONS = {
    # 'San Mateo': '130', # the office ID obtained by inspecting the xpath, this is what selenium uses to identify the correct option
    'Redwood City': '548',
    'San Jose': '516',
    'Santa Clara': '632',
    'Las Gatos': '640'
}
PROFILE = {
    'first_name': 'Zhao',
    'last_name': 'Dong',
    'tel_prefix': '412',
    'tel_suffix1': '608',
    'tel_suffix2': '3112',
    'email': 'joe.pekdz@gmail.com'
    #    'mm': '09',
    #    'dd': '01',
    #    'yyyy': '1994',
    #    'dl_number': 'Y4497779'
}

