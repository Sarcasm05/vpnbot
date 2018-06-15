# -*- coding: utf-8 -*-

#update monsherko
import sqlite3

import MySQLdb

class Liter:

    def __init__(self, database):
        self.connection =  MySQLdb.connect(host='localhost',user='root', db='activeDB')

        self.cursor = self.connection.cursor()

    def select_all(self):
        #Получаем все строки
        with self.connection:
            return self.cursor.execute('SELECT * FROM FileOVPN').fetchall()

    def select_single(self, rownum):
        #Получаем одну строку с номером rownum из FileOVPN
        with self.connection:
            return self.cursor.execute('SELECT * FROM FileOVPN WHERE id = ?', (rownum,)).fetchall()[0]

    def select_country(self):
        #выбираем все страны
        with self.connection:
            return self.cursor.execute('SELECT countryName FROM FileOVPN').fetchall()

    def in_country(self, call):
        with self.connection:
            return self.cursor.execute('SELECT * FROM FileOVPN WHERE countryName = ?', (call,)).fetchall()

    def select_state(self, country):
        #выбираем все штаты
        with self.connection:
            return self.cursor.execute('SELECT stateProv FROM FileOVPN WHERE countryName = ?',(country,)).fetchall()

    def in_state(self, call):
        with self.connection:
            return self.cursor.execute('SELECT * FROM FileOVPN WHERE stateProv = ?', (call,)).fetchone()

    def select_city(self, state):
        #выбираем все города
        with self.connection:
            return self.cursor.execute('SELECT city FROM FileOVPN WHERE stateProv = ?',(state,)).fetchall()

    def in_city(self, call):
        with self.connection:
            return self.cursor.execute('SELECT * FROM FileOVPN WHERE city = ?', (call,)).fetchone()

    def in_zip(self, call):
        with self.connection:
            return self.cursor.execute('SELECT * FROM FileOVPN WHERE zipCode = ?', (call,)).fetchone()

    def select_vpn(self, call):
        with self.connection:
            return self.cursor.execute('SELECT * FROM FileOVPN WHERE zipCode = ?', (call,)).fetchone()

    def our_choice(self, city):
        with self.connection:
            return self.cursor.execute('SELECT zipCode FROM FileOVPN WHERE city = ?',(city,)).fetchall()

    def count_rows(self):
        #Считаем количество строк
        with self.connection:
            result = self.cursor.execute('SELECT * FROM FileOVPN').fetchall()

    def in_city(self, call):
        with self.connection:
            return self.cursor.execute('SELECT * FROM FileOVPN WHERE city = ?', (call,)).fetchone()

    def in_zip(self, call):
        with self.connection:
            return self.cursor.execute('SELECT * FROM FileOVPN WHERE zipCode = ?', (call,)).fetchone()

    def select_namefile_none(self, call):
        with self.connection:
            return self.cursor.execute('SELECT file_name FROM FileOVPN WHERE city = ?', (call,)).fetchone()

    def select_namefile(self, call):
        with self.connection:
            return self.cursor.execute('SELECT file_name FROM FileOVPN WHERE city = ?', (call,)).fetchone()

    def our_choice(self, city):
        with self.connection:
            return self.cursor.execute('SELECT zipCode FROM FileOVPN WHERE city = ?',(city,)).fetchall()

    def count_rows(self):
        #Считаем количество строк
        with self.connection:
            result = self.cursor.execute('SELECT * FROM FileOVPN').fetchall()
            return len(result)

    def exist(self, call):
        #просто нужная хуйня
        with self.connection:
            return self.cursor.execute('SELECT ? FROM FileOVPN',(call,)).fetchall()

    def add_user(self, user_id):
        #добавляем пользователя
        with self.connection:
            return self.cursor.execute('INSERT INTO users VALUES(?,?,?,?,?)',(user_id, 0, 'null',0,0));

    def select_user(self, user_id):
        #выбираем пользователя
        with self.connection:
            return self.cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,)).fetchone()

    def select_user_state(self, user_id):
        #узнаем статус пользователя
        with self.connection:
            return self.cursor.execute('SELECT state FROM users WHERE user_id = ?', (user_id,)).fetchone()[0]

    def select_user_choice(self, user_id):
        #узнаем статус пользователя
        with self.connection:
            return self.cursor.execute('SELECT choice FROM users WHERE user_id = ?', (user_id,)).fetchone()[0]

    def select_user_token(self, user_id):

        with self.connection:
            return self.cursor.execute('SELECT token FROM users WHERE user_id = ?', (user_id,)).fetchone()[0]

    def select_user_payment_status(self, user_id):

        with self.connection:
            return self.cursor.execute('SELECT payment_status FROM users WHERE user_id = ?', (user_id,)).fetchone()[0]


    def update_user_state(self, user_id, status):
        #обновляем статус пользователя
        with self.connection:
            self.cursor.execute('UPDATE users SET state = ? WHERE user_id= ?',(status, user_id))

    def update_user_choice(self, user_id, choice):
        #обновляем статус пользователя
        with self.connection:
            self.cursor.execute('UPDATE users SET choice = ? WHERE user_id= ?',(choice[0], user_id))

    def update_user_token(self, user_id, token):

        with self.connection:
            self.cursor.execute('UPDATE users SET token = ? WHERE user_id= ?',(token, user_id))

    def update_user_payment_status(self, user_id, status):

        with self.connection:
            self.cursor.execute('UPDATE users SET payment_status = ? WHERE user_id= ?',(status, user_id))

    def choice(self, user_id):
        with self.connection:
            choice  = self.cursor.execute('SELECT choice FROM users WHERE user_id = ?', (user_id,)).fetchone()[0]
            if choice == 'null' :
                return 'null'
            else:
                country = self.cursor.execute('SELECT countryName FROM FileOVPN WHERE file_name = ?', (choice,)).fetchone()[0]
                state = self.cursor.execute('SELECT stateProv FROM FileOVPN WHERE file_name = ?', (choice,)).fetchone()[0]
                city = self.cursor.execute('SELECT city FROM FileOVPN WHERE file_name = ?', (choice,)).fetchone()[0]
            return country + ', ' + state + ', ' + city

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()
