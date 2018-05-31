# -*- coding: utf-8 -*-
import sqlite3

class liter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def add_filename(self, filename, login, password, site, ip, continentCode, continentName, countryCode, countryName, isEuMember, currencyCode, currencyName, phonePrefix, languages, stateProv, district, city, geonameId, latitude, longitude, gmtOffset, timeZone, asNumber, asName, isp, organization, isCrawler, isProxy, threatLevel):
        #добавляем пользователя
        with self.connection:
            return self.cursor.execute('INSERT INTO vpns VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(filename, login, password, site, ip, continentCode, continentName, countryCode, countryName, isEuMember, currencyCode, currencyName, phonePrefix, languages, stateProv, district, city, geonameId, latitude, longitude, gmtOffset, timeZone, asNumber, asName, isp, organization, isCrawler, isProxy, threatLevel,)); 

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()
    
