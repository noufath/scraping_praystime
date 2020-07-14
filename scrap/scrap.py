from scrap.getdata import GetData


class Scrap():
    def __init__(self,url_name):
        self.Url = url_name

    def AskCityCode(self):
        return GetData(self.Url).citylist()

    def GetWaktuSholat(self):
        return GetData(self.Url).get_waktusholat()

    def GetJadwalSholat(self):
        return GetData(self.Url).get_jadwalsholat()

    def DispJadwalSholat(self):
        return GetData(self.Url).disp_jadwalsholat()