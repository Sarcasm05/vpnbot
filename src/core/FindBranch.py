import MySQLdb

class AdoptBranch:
    def __init__(self):
        self.connection =  MySQLdb.connect(host='localhost',user='root', db='activeDB')
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self.cursor
    def __exit__(self, type, value, traceback):
        self.connection.commit()
        self.connection.close()

    @staticmethod
    def select_country():
        return 'select distinct countryName from FileOVPN'
    @staticmethod
    def select_state(country):
        return 'select stateProv FROM FileOVPN WHERE countryName = \'%s\'' % (country)

    @staticmethod
    def in_country(call):
        return 'select * from FileOVPN WHERE countryName = \'%s\'' % (call)
    @staticmethod
    def select_city(state):
        return 'select city FROM FileOVPN WHERE stateProv = \'%s\'' % (state)

    @staticmethod
    def in_state(call):
        return 'select * FROM FileOVPN WHERE stateProv = \'%s\'' % (call)

    @staticmethod
    def in_city(call):
        return 'select * FROM FileOVPN WHERE city = \'%s\'' % (call)

    @staticmethod
    def add_user(user_id):
        return 'insert into User VALUES(%d,%d)' % (user_id,0)

    @staticmethod
    def select_user(user_id):
        return 'select * FROM User WHERE user_id = %d' % (user_id)

    @staticmethod
    def select_user_state(user_id):
        return 'select status FROM User WHERE user_id = %d' % (user_id)

    @staticmethod
    def update_user_state(user_id, status):
        return 'update User SET status = %d WHERE user_id= %d' % (status, user_id)

    @staticmethod
    def get_payments(user_id):
        return 'select * from Payment where user_id = %d and status = 1' % (user_id)

    @staticmethod
    def get_filename(val):
        return 'select file_name from FileOVPN where city = \'%s\' or countryName = \'%s\' or stateProv = \'%s\'' % (val,val,val)

    @staticmethod
    def add_pay(token, user_id, file_name, data_req, status):
        return 'insert into Payment (token, user_id, file_name, data_req, status)  VALUES(\'%s\', %d, \'%s\', \'%s\', %d)' % (token, user_id, file_name, data_req, status)
