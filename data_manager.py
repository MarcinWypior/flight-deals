import os
import requests


class DataManager:
    def __init__(self):
        self.sheety_username = os.getenv("sheety_username")
        self.sheety_password = os.getenv("sheety_password")
        self.ednpoint = "https://api.sheety.co/2842257f9e35427dabf20d449c12c599/flightDeals/prices"
        self.auth = (
            self.sheety_username,
            self.sheety_password,
        )

    def getdata(self):
        url_sheety_get = self.ednpoint
        response = requests.get(url=url_sheety_get, auth=self.auth)
        return response.json()

    def editdata(self, iata_code: str, row_id: int):
        params = {
            "price": {
                "iataCode": iata_code,
                #"lowestPrice":iata_code,
                #"city" : iata_code
            }
        }
        response = requests.put(url=f"{self.ednpoint}/{row_id}", json=params, auth=self.auth)
        print(response)

if __name__ == "__main__" :
    my_datamanager = DataManager()
    my_datamanager.editdata("IataCode", 2)
