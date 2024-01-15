
import requests
from twilio.rest import Client

api_key = "a30665999b7a65562ce8ccc90f"  # openweathermap.org will not work use your own

acc_sid = "AC22cca78fb4a9672792faaf474"  # console.twilio.com will not work use your own
auth_token = "9f61f801a98a7f4151e12c3"  # console.twilio.com will not work use your own


my_lat = 19.154689  # latlong.com
my_long = 76.210251

parameters = {
    "lat": 13.756331,
    "lon": 100.501762,
    "appid": api_key,
    "exclude": "currently,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()

weather_slice = [weather_data["hourly"][i]["weather"] for i in range(12)]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data[0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # to run this code on cloud goto pythonanywhere.com
    # and refer to day 35 second last lesson
    client = Client(acc_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. remember to bring an umbrella ☔",
        from_="+1848420985",
        to="+917385348373"
    )

    print(message.status)


