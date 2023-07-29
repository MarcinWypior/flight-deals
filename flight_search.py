import requests


class FlightSearch:
    def get_categories(self):
        import requests
        url = "https://travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com/v1/prices/monthly"
        querystring = {"destination": " MOW", "origin": "LED", "length": "3", "currency": "RUB"}
        headers = {
            "X-Access-Token": "<REQUIRED>",
            "X-RapidAPI-Key": "82d0e9f98fmsh75408924d4ce198p136f97jsn17ebda80ba66",
            "X-RapidAPI-Host": "travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        print(response.json())

flight_serach = FlightSearch()
flight_serach.get_categories()