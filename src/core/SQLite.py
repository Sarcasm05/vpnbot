# -*- coding: utf-8 -*-

#update monsherko
import sqlite3

class Liter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def select_all(self):
        #Получаем все строки
        with self.connection:
            return self.cursor.execute('SELECT * FROM vpns').fetchall()

    def select_single(self, rownum):
        #Получаем одну строку с номером rownum из vpns
        with self.connection:
            return self.cursor.execute('SELECT * FROM vpns WHERE id = ?', (rownum,)).fetchall()[0]

    def select_country(self):
        #выбираем все страны
        with self.connection:
            return self.cursor.execute('SELECT country FROM vpns').fetchall()

    def in_country(self, call):
        with self.connection:
            return self.cursor.execute('SELECT * FROM vpns WHERE country = ?', (call,)).fetchall()

    def select_state(self, country):
        #выбираем все штаты
        with self.connection:
            return self.cursor.execute('SELECT state FROM vpns WHERE country = ?',(country,)).fetchall()

    def in_state(self, call):
        with self.connection:
            return self.cursor.execute('SELECT * FROM vpns WHERE state = ?', (call,)).fetchone()

    def select_city(self, state):
        #выбираем все города
        with self.connection:
            return self.cursor.execute('SELECT city FROM vpns WHERE state = ?',(state,)).fetchall()

    def in_city(self, call):
        with self.connection:
            return self.cursor.execute('SELECT * FROM vpns WHERE city = ?', (call,)).fetchone()

    def in_zip(self, call):
        with self.connection:
            return self.cursor.execute('SELECT * FROM vpns WHERE zip = ?', (call,)).fetchone()

    def select_vpn(self, call):
        with self.connection:
            return self.cursor.execute('SELECT * FROM vpns WHERE zip = ?', (call,)).fetchone()

    def our_choice(self, city):
        with self.connection:
            return self.cursor.execute('SELECT zip FROM vpns WHERE city = ?',(city,)).fetchall()

    def count_rows(self):
        #Считаем количество строк
        with self.connection:
            result = self.cursor.execute('SELECT * FROM vpns').fetchall()
            return len(result)

    def exist(self, call):
        #просто нужная хуйня
        with self.connection:
            return self.cursor.execute('SELECT ? FROM vpns',(call,)).fetchall()

    def add_user(self, user_id):
        #добавляем пользователя
        with self.connection:
            return self.cursor.execute('INSERT INTO users VALUES(?,?,?)',(user_id, 0, 'null'));

    def select_user(self, user_id):
        #выбираем пользователя
        with self.connection:
            return self.cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,)).fetchone()

    def select_user_state(self, user_id):
        #узнаем статус пользователя
        with self.connection:
            return self.cursor.execute('SELECT state FROM users WHERE user_id = ?', (user_id,)).fetchone()[0]

    def update_user_state(self, user_id, status):
        #обновляем статус пользователя
        with self.connection:
            self.cursor.execute('UPDATE users SET state = ? WHERE user_id= ?',(status, user_id))

    def update_user_choice(self, user_id, choice):
        #обновляем статус пользователя
        with self.connection:
            self.cursor.execute('UPDATE users SET choice = ? WHERE user_id= ?',(choice, user_id))

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()