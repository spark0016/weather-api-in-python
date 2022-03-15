import requests

key = "49001fce1187e707f900349b48d202e0"

_type = input("The type: ")
place = input("Place: ")

if _type == "CURRENT":
    respone = requests.get(f"http://api.weatherstack.com/current?access_key={key}&query={place}")

if _type == "HISTORICAL":
    _date = input("Date: ")
    respone = requests.get(f"http://api.weatherstack.com/historical?access_key={key}&query={place}&historical_date={_date}")

if _type == "TIME-SERIEAS":
    historical_date_start = input()
    historical_date_end = input()
    respone = requests.get(f"http://api.weatherstack.com/historical?access_key={key}&query={place}&historical_date_start={historical_date_start}&historical_date_end={historical_date_end}")

if _type == "FORECAST":
    respone = requests.get(f"http://api.weatherstack.com/forecast?access_key={key}&query={place}")

result = respone.text


class Data:
    def __init__(self):
        return result


print(result)
