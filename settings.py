SLACK_CHANNEL = 'bot' # this should be the slack channel which you want to send messages to
DRIVE_URL = 'https://www.dmv.ca.gov/wasapp/foa/clear.do?goTo=driveTest'  # behind the wheel test
WRITEN_URL = 'https://www.dmv.ca.gov/wasapp/foa/clear.do?goTo=officeVisit&localeName=en' # permit test
TIMERANGE = 2 # maximum days from ealiest day
EARLESTDAY = "May 25, 2018" # Earliest available day
DAY_PERIOD = 20 # seconds between each fetching at daytime
NIGHT_PERIOD = 150 # seconds between each fetching at nighttime
LOCATIONS = {
    'Redwood City': '548', # the office ID obtained by inspecting the xpath
    'San Jose': '516',
    'Santa Clara': '632',
    # 'Las Gatos': '640',
    # 'San Jose DLPC': '645'
}
PROFILE = {
    'first_name': 'Zhao',
    'last_name': 'Dong',
    'tel_prefix': '412',
    'tel_suffix1': '608',
    'tel_suffix2': '3112',
    'email': 'joe.pekdz@gmail.com',
    'mm': '09',
    'dd': '01',
    'yyyy': '1994',
    'dl_number': 'Y5306083'
}