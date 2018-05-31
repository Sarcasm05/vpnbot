# -*- coding: utf-8 -*-
import csv
from config import DATABASE, CSV_NAME
from SQLite import liter



def add_filename(filename, login, password, site, ip, continentCode, continentName, countryCode, countryName, isEuMember, currencyCode, currencyName, phonePrefix, languages, stateProv, district, city, geonameId, latitude, longitude, gmtOffset, timeZone, asNumber, asName, isp, organization, isCrawler, isProxy, threatLevel):
    db = liter(DATABASE)
    db.add_filename(filename, login, password, site, ip, continentCode, continentName, countryCode, countryName, isEuMember, currencyCode, currencyName, phonePrefix, languages, stateProv, district, city, geonameId, latitude, longitude, gmtOffset, timeZone, asNumber, asName, isp, organization, isCrawler, isProxy, threatLevel)
    db.close()

def exist(name,string, word):
    if string in word:
        row = word.split(': ')
        try:
            name = row[1]
            #name = row[1]
            #print(name)
        except IndexError as e:
            name = row[0]
        
        

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
           
            #exist(continentCode,"continentCode", word)
            if "continentCode" in word:
                row = word.split(': ')
                continentCode = row[1]
            if "continentName" in word:
                row = word.split(': ')
                continentName = row[1]
            if "countryCode" in word:
                row = word.split(': ')
                countryCode = row[1]
            if "countryName" in word:
                row = word.split(': ')
                countryName = row[1]
            if "isEuMember" in word:
                row = word.split(': ')
                isEuMember = row[1]
            if "currencyCode" in word:
                row = word.split(': ')
                currencyCode = row[1]
            if "phonePrefix" in word:
                row = word.split(': ')
                phonePrefix = row[1]
            if "languages" in word:
                row = word.split(': ')
                languages = row[1]
            if "stateProv" in word:
                row = word.split(': ')
                stateProv = row[1]
            if "district" in word:
                row = word.split(': ')
                district = row[1]
            if "city" in word:
                try:
                    row = word.split(': ')
                    city = row[1]
                except IndexError as e:
                    city = row[0]
            if "geonameId" in word:
                row = word.split(': ')
                geonameId = row[1]
            if "latitude" in word:
                row = word.split(': ')
                latitude = row[1]
            if "longitude" in word:
                row = word.split(': ')
                longitude = row[1]
            if "gmtOffset" in word:
                row = word.split(': ')
                gmtOffset = row[1]
            if "timeZone" in word:
                row = word.split(': ')
                timeZone = row[1]
            if "asNumber" in word:
                row = word.split(': ')
                asNumber = row[1]
            if "asName" in word:
                row = word.split(': ')
                asName = row[1]
            if "isp" in word:
                try:
                    row = word.split(': ')
                    isp = row[1]
                except IndexError as e:
                    isp = row[0]
            if "isCrawler" in word:
                row = word.split(': ')
                isCrawler = row[1]
            if "isProxy" in word:
                row = word.split(': ')
                isProxy = row[1]
            if "threatLevel" in word:
                row = word.split(': ')
                threatLevel = row[1]
            if "organization" in word:
                row = word.split(': ')
                organization = row[1]
            if "currencyName" in word:
                row = word.split(': ')
                currencyName = row[1]
           
            
        add_filename(filename, login, password, site, ip, continentCode, continentName, 
                    countryCode, countryName, isEuMember, currencyCode, currencyName, 
                    phonePrefix, languages, stateProv, district, city, geonameId, latitude, 
                    longitude, gmtOffset, timeZone, asNumber, asName, isp, organization, 
                    isCrawler, isProxy, threatLevel)
              
 
if __name__ == "__main__":
    csv_path = CSV_NAME
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)