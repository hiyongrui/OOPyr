from Clinic import Clinic

class North(Clinic):
    #def __init__(self, title, publisher, status, created_by, category, type, frequency):
    def __init__(self, title, address, phone, openingHour, busNo, mrtStation, hospital, created_by,areaName):
        Clinic.__init__(self, title,address,phone,openingHour,busNo,mrtStation,hospital,created_by)
        self.__areaName = areaName

    def get_areaName(self):
        return self.__areaName

    def set_areaName(self,areaName):
        self.__areaName = areaName
