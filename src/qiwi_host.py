"""
    Программа запускается отдельным процессом. Изменяет состояние status при успешной оплате
"""

from core import WalletQiwi



import time
import config
from core import WalletQiwi
QApi = WalletQiwi.QApi
import datetime
import MySQLdb

QApi = WalletQiwi.QApi
def f():
    try:
        db = MySQLdb.connect(host='localhost',user='root', db='activeDB')



        data2 ='select user_id, token, name_ovpn from payment where status is  NULL and datatime > \'%s\' order by datatime;'
        date2 = (datetime.datetime.now()-datetime.timedelta(minutes=4)).strftime("%Y-%m-%d %H:%M:%S")

        cursor = db.cursor()
        cursor.execute('use activeDB;')
        cursor.execute(data2 % date2)
        time_delta = 0
        for user in cursor.fetchall():
            print(str(user)  +  ' ')
            ext = QApi(phone=config.phone, token=config.token_qiwi)
            comment = ext.bill(comment=user[1])
            print(comment)
            print(len(comment))
            ext.run()

            if ext.check_info(comment):
                cursor.execute('update payment set status = 1 where user_id = %s' % str(user[0]))
                print('YEEES')


                db.commit()

                ext.close()

                return user[0]
            time.sleep(5)
    except:
        print('error connection mysql')
