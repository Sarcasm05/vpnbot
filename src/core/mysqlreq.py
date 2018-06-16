
import MySQLdb

class MyLiter:
    def __init__(self, database):
        self.connection =  MySQLdb.connect(host='localhost',user='root', db='activeDB')
        self.cursor = self.connection.cursor()
    def select_country(self):
        #выбираем все страны
        with self.connection:
            self.cursor.execute('select countryName FROM FileOVPN;')
            return  self.cursor.fetchall()
