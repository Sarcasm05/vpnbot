import MySQLdb



class Msq:

    def __init__(self, database):
        self.connection =  MySQLdb.connect(host='localhost',user='root', db='activeDB')
        self.cursor = self.connection.cursor()


    def select_country(self):
        #выбираем все страны
        with self.connection:
            self.cursor.execute('select distinct countryName from FileOVPN')
            return self.cursor.fetchall()

    def in_country(self, call):
        with self.connection:
            self.cursor.execute('select * from FileOVPN where countryName = ?', (call,))
            return self.cursor.fetchall()

    def select_state(self, country):
        #выбираем все штаты
        with self.connection:
            self.cursor.execute('select stateProv from FileOVPN where countryName = ?', (country,))
            return self.cursor.fetchall()

    def in_state(self, call):
        with self.connection:
            self.cursor.execute('select * from FileOVPN where stateProv = ?', (call,))
            return self.cursor.fetchone()

    def select_city(self, state):
        #выбираем все города
        with self.connection:
            self.cursor.execute('select city from FileOVPN where stateProv = ?', (state,))
            return self.cursor.fetchall()

    def in_city(self, call):
        with self.connection:
            self.cursor.execute('select * from FileOVPN where city = ?', (call,))
            return self.cursor.fetchone()



    def update_user_state(self, user_id, status):
        with self.connection:
            self.cursor.execute('update User set status = ? where user_id = ?', (status, user_id))
            self.cursor.commit()



    def select_user_state(self, user_id):
        #узнаем статус пользователя
        with self.connection:
            self.cursor.execute('select state FROM users WHERE user_id = ?', (user_id,))
            return self.cursor.fetchone()[0]

    def choice(self, user_id):
        print('yspeh')
