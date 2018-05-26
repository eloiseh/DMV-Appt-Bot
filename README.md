# Stalk the DMV - Advanced Edition

[Original version](https://github.com/thisisandreeeee/stalk-the-DMV) only supports querying DMV available date for driving test appointment, this advanced version supports making appointment for both writen test and driving test automatically, the location and date can be set as you desired, the confirmation page's screenshot will be saved.

## Installation and Usage
Grab your local copy.
```
https://github.com/Pekdz/stalk-the-DMV.git
```
Install the dependencies, which includes python libraries and phantomjs.
Only available in Linux, no Mac because Mac doesn't support virtual display to save screenshot(maybe).
Recommended to create a free linux machine in cloud(e.g., AWS)
```
sudo apt-get install xvfb xserver-xephyr
sudo pip install -r requirements.txt

cd ~
export PHANTOM_JS="phantomjs-2.1.1-linux-x86_64"
wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2
sudo tar xvjf $PHANTOM_JS.tar.bz2
sudo mv $PHANTOM_JS /usr/local/share
sudo ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin
```
Obtain a [slack token](https://api.slack.com/docs/oauth-test-tokens). Then, create a config file - this should be kept hidden! In the current directory, enter the following:
```
echo "SLACK_TOKEN='your-token-here'" >> creds.py
```
Don't forget to replace the string above with your own slack token. When that is done, open `settings.py` and update it with your information.
```python
SLACK_CHANNEL = 'bot'       # the slack channel which you want to send messages to
DRIVE_URL = 'https://www.dmv.ca.gov/wasapp/foa/clear.do?goTo=driveTest'                  # driving test
WRITEN_URL = 'https://www.dmv.ca.gov/wasapp/foa/clear.do?goTo=officeVisit&localeName=en' # writen test
TIMERANGE = 2               # maximum days from ealiest day
EARLESTDAY = "May 25, 2018" # Earliest available day
DAY_PERIOD = 20             # seconds between each fetching at daytime
NIGHT_PERIOD = 150          # seconds between each fetching at nighttime
LOCATIONS = {               # the office ID obtained by inspecting the xpath
    'Redwood City': '548',
    'San Jose': '516',
    'Santa Clara': '632',
    'Las Gatos': '640',
    'San Jose DLPC': '645'
}
PROFILE = {
    'first_name': 'xxx',
    'last_name': 'xxx',
    'tel_prefix': 'xxx',
    'tel_suffix1': 'xxx',
    'tel_suffix2': 'xxxx',
    'email': 'xxxx@gmail.com',
    'mm': 'xx',
    'dd': 'xx',
    'yyyy': 'xxxx',
    'dl_number': 'XXXXXX'
}
```
Run the bot.
```
python main.py
```

## Caveats
This is not a hack, all it does is automating an otherwise tedious process of page refreshing and manual monitoring. 
Only used for personal non-commercial purpose.
