# -*- coding: utf-8 -*-
import sqlite3

class liter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def select_all(self):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM vpns').fetchall()

    def select_single(self, rownum):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            return self.cursor.execute('SELECT * FROM vpns WHERE id = ?', (rownum,)).fetchall()[0]

    def select_country(self):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            return set(self.cursor.execute('SELECT country FROM vpns').fetchall()) 

    def select_state(self):
        
        with self.connection:
            return set(self.cursor.execute('SELECT state FROM vpns').fetchall()) 

    def select_city(self):
        
        with self.connection:
            return set(self.cursor.execute('SELECT city FROM vpns').fetchall())

    def select_country(self):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            return set(self.cursor.execute('SELECT country FROM vpns').fetchall())       

    def count_rows(self):
        """ Считаем количество строк """
        with self.connection:
            result = self.cursor.execute('SELECT * FROM vpns').fetchall()
            return len(result)

    def exist(self, call):
        with self.connection:
            return self.cursor.execute('SELECT ? FROM vpns',(call,)).fetchall()

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()
    """
    def update(self, id, task_id):
        
        with self.connection:
            self.cursor.execute('UPDATE users SET task_status="YES" WHERE id= ?',(id, ))
            self.cursor.execute('UPDATE users SET task_id=? WHERE id= ?',(task_id,id, ))        
    """
