from scrap.scrap import Scrap


class choice(object):
    '''
        Class Menu Selection
    '''

    def __init__(self,menu_name):
        self.menu_name = menu_name

    def on_selection(self, menu, index):
        url = "https://jadwalsholat.pkpu.or.id?id="
        if index == 0:
            sc = input("Input kode Kota =")
            url_withcity = url + sc

            print('\n', Scrap(url_withcity).DispJadwalSholat(), '\n')

            menu.input()

        else:
            citylist = Scrap(url).AskCityCode()
            for key, val in citylist.items():
                print(f'{key} - {val}')

            # Input Kode Kota Pilihan #
            sc = input("Input kode Kota =")
            url_withcity = url + sc

            print('\n',Scrap(url_withcity).DispJadwalSholat(),'\n')

            menu.input()













