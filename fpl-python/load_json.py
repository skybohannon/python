import urllib.request
import json
from bs4 import BeautifulSoup

FPL_URL = "https://fantasy.premierleague.com/drf/"
USER_SUMMARY_SUBURL = "element-summary/"
LEAGUE_STANDING_SUBURL = "leagues-classic-standings/"
TEAM_ENTRY_SUBURL = "entry/"
GW_NUMBER = 1
EVENT_SUBURL = "event/" + str(GW_NUMBER) + "/picks"
USER_SUMMARY_URL = FPL_URL + USER_SUMMARY_SUBURL
LEAGUE_STANDING_URL = FPL_URL + LEAGUE_STANDING_SUBURL
ID_TEST = 1
league_id = 116940

urlData = "https://fantasy.premierleague.com/drf/bootstrap-static"
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
print(json.loads(data.decode(encoding)))

with open('data.txt', 'w') as outfile:
    json.dump(data.decode(encoding), outfile, ensure_ascii=False)