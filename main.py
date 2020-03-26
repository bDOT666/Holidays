import requests as rq
import json
import pprint as pp
import webbrowser as ww
from datetime import datetime, timedelta


url = "https://calendarific.com/api/v2/holidays/"

params = {
    "api_key": "Api_Key",
    "country": "pl",
    "year": datetime.today().year
#    "month": datetime.today().month
}


def download_holidays_for_this_month(link, paramss):
    return rq.get(link, paramss)


def get_holidays_fromjson(request):
    try:
        holidays = request.json()
    except json.decoder.JSONDecodeError:
        print("Niepoprany format")
    else:
        return holidays["response"]["holidays"]


r = download_holidays_for_this_month(url, params)
holidays = get_holidays_fromjson(r)
# pp.pprint(holidays)

h = []

for holiday in holidays:
    holidays_to_print = {
    "name": holiday["name"],
    "date":   holiday["date"]["iso"][0:10],
    "description":   holiday["description"],
    "type": holiday["type"]
    }
    h.append(holidays_to_print)

pp.pprint(h)
