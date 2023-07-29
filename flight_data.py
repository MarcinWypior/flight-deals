import requests
import os
class FlightData:
    def __init__(self):
        self.url="http://api.aviationstack.com/v1/flights"
        self.aviationstack_key='d507a8851c00cece9330822322bb4c8e'
        self.iata_code_london="LHR"

    def get_info(self):
        params = {
            'access_key': self.aviationstack_key,
            'dep_iata':"LHR",
            'arr_iata':"CDG",
        }
        response = requests.get(url=self.url, params=params)
        return response

if __name__ == "__main__":
    flightdata = FlightData()
    print(flightdata.aviationstack_key)
    print(flightdata.get_info().json())