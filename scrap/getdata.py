import requests
from bs4 import BeautifulSoup
# import pandas as pd


class GetData():
    def __init__(self, url_address):
        self.url_address = url_address
        self.url_response = requests.get(url_address)

    def scrap_status(self):
        return self.url_response.status_code

    def parsed_html(self):
        return BeautifulSoup(self.url_response.content, 'html.parser')

    def parsed_body(self):
        return self.parsed_html().find('body')

    def listkota(self):
        """
        Get List Kota
        """

        # Use panda data frame
        #city_collect = self.parsed_body().find('select', class_="inputcity")
        #options = city_collect.find_all('option')
        #city = [y.text for y in options]
        #value = [o.get("value") for o in options]
        #list_kota =  pd.DataFrame({'kode_kota': values,'nama_kota': options1})


        # Use Dictionary
        options = self.parsed_body().select('select[name="kota"] option')
        city = [y.text for y in options]
        value = [o.get("value") for o in options]

        # store to dictionary
        list_kota = dict(zip(value, city))

        return list_kota
