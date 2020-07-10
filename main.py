from scrap.getdata import GetData
from scrap.url import Url
import scrap.getdata


"""
Scraping Pray's Time for indonesia. source data taken from http://pkpu.go.id
"""

print("## Info Jadwal Sholat di Indonesia ##")

url = Url("https://jadwalsholat.pkpu.or.id/?id=")
options = ["Input Kode Kota", "Lihat Kode Kota"]

for i in range(len(options)):
    print(str(i + 1) + ":", options[i])

# Take user input and get the corresponding item from the list
inp = int(input("Input a Number : "))

if inp in range(1,len(options)+1):
    if inp == 1:
        # Input Kode Kota #
        kode_kota = input("kode_kota :")
        print(url.name()+kode_kota)
    else:
        "List Kode Kota"
        list_kota = GetData(url.name()).listkota()
        for key, val in list_kota.items():
            print(f'{key} - {val}')








else:
    print("Invalid Number")



