import requests
from bs4 import BeautifulSoup
import pandas as pd


class GetData():
    def __init__(self, url_name):
        self.url = url_name
        self.url_response = requests.get(self.url)

    def scrap_status(self):
        return self.url_response.status_code

    def parsed_html(self):
        return BeautifulSoup(self.url_response.content, 'html.parser')

    def parsed_body(self):
        return self.parsed_html().find('body')

    def citylist(self):
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
        citylist = dict(zip(value, city))
        return citylist

    def get_waktusholat(self):
        ws_header = self.parsed_body().find('tr','table_header')
        ws_waktusholat = ws_header.find_all('b')
        waktusholat = [y.text for y in ws_waktusholat]
        return waktusholat

    def get_jadwalsholat(self):
        js_raw = self.parsed_body().find('tr','table_highlight')
        js_jamsholat = js_raw.find_all('td')
        jamsholat = [y.text for y in js_jamsholat]
        return jamsholat

    def disp_jadwalsholat(self):
        waktu_sholat = self.get_waktusholat()
        jam_sholat = self.get_jadwalsholat()

        return pd.DataFrame({'Waktu SHolat': waktu_sholat[1:], 'Jam Sholat': jam_sholat[1:]})
