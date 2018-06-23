import MySQLdb

class AdoptBranch:
    def __init__(self):
        self.connection =  MySQLdb.connect(host='localhost',user='root', db='activeDB')
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self.cursor
    def __exit__(self, type, value, traceback):
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
        return 'select * FROM FileOVPN WHERE city = %s' % (call)

    @staticmethod
    def add_user(user_id):
        return 'insert into User VALUES(%d,%d)' % (user_id,0)

    @staticmethod
    def select_user(user_id):
        return 'select * FROM User WHERE user_id = %s' % (user_id)

    @staticmethod
    def select_user_state(user_id):
        return 'select status FROM User WHERE user_id = %s' % (user_id)

    @staticmethod
    def update_user_state(user_id, status):
        return 'update User SET status = %d WHERE user_id= %d' % (status, user_id)
