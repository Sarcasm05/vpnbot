# -*- coding: utf-8 -*-
import csv
from config import DATABASE, CSV_NAME
from SQLite import liter



def add_filename(filename, login, password, site, ip, continentCode, continentName, countryCode, countryName, isEuMember, currencyCode, currencyName, phonePrefix, languages, stateProv, district, city, geonameId, latitude, longitude, gmtOffset, timeZone, asNumber, asName, isp, organization, isCrawler, isProxy, threatLevel):
    db = liter(DATABASE)
    db.add_filename(filename, login, password, site, ip, continentCode, continentName, countryCode, countryName, isEuMember, currencyCode, currencyName, phonePrefix, languages, stateProv, district, city, geonameId, latitude, longitude, gmtOffset, timeZone, asNumber, asName, isp, organization, isCrawler, isProxy, threatLevel)
    db.close()

def exist(word, string):
    if word in string:
        
        """
        newrow = ""
        flag = False
        for elem in word:
            if elem == ":":
                flag = True
            if flag == True:
                newrow += elem
        """
        row = string.split(': ')
        return row[1]

def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        filename = row[0]
        login = row[1]
        password = row[2]
        site = row[3]
        ip = row[4]
        continentCode = "none"
        continentName = "none"
        countryCode = "none"
        countryName = "none"
        isEuMember = "none"
        currencyCode = "none"
        currencyName = "none"
        phonePrefix = "none"
        languages = "none"
        stateProv = "none"
        district = "none"
        city = "none"
        geonameId = "none"
        latitude = "none"
        longitude = "none"
        gmtOffset = "none"
        timeZone = "none"
        asNumber = "none"
        asName = "none"
        isp = "none"
        organization = "none"
        isCrawler = "none"
        isProxy = "none"
        threatLevel = "none"
        for word in row:
            continentCode = exist("continentCode", word)
            continentName = exist("continentName", word)
            countryCode = exist("countryCode", word)
            scountryNametring = exist("countryName", word)
            isEuMember = exist("isEuMember", word)
            currencyCode = exist("currencyCode", word)
            currencyName = exist("currencyName", word)
            phonePrefix = exist("phonePrefix", word)
            languages = exist("languages", word)
            stateProv = exist("stateProv", word)
            district = exist("district", word)
            city = exist("city", word)
            geonameId = exist("geonameId", word)
            latitude = exist("latitude", word)
            longitude = exist("longitude", word)
            gmtOffset = exist("gmtOffset", word)
            sttimeZonering = exist("timeZone", word)
            asNumber = exist("asNumber", word)
            asName = exist("asName", word)
            isp = exist("isp", word)
            organization = exist("organization", word)
            isCrawler = exist("isCrawler", word)
            isProxy = exist("isProxy", word)
            asNumber = exist("asNumber", word)
            threatLevel = exist("threatLevel", word)
            
        """
        add_filename(filename, login, password, site, ip, continentCode, continentName, 
                    countryCode, countryName, isEuMember, currencyCode, currencyName, 
                    phonePrefix, languages, stateProv, district, city, geonameId, latitude, 
                    longitude, gmtOffset, timeZone, asNumber, asName, isp, organization, 
                    isCrawler, isProxy, threatLevel)
        """       
 
if __name__ == "__main__":
    csv_path = CSV_NAME
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)