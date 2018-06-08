"""
    Программа запускается отдельным процессом. Изменяет состояние status при успешной оплате
"""

from core import WalletQiwi


import MySQLdb
import datetime
import time
import config

QApi = WalletQiwi.QApi

def find(host, user, db_name):

    try:
        db = MySQLdb.connect(host,user, db_name)
    except:
        print('error connection mysql')


    data ='select user_id, token, name_ovpn from payment where status is  NULL and datatime > \'%s\' order by datatime;'
    date = (datetime.datetime.now()-datetime.timedelta(minutes=4)).strftime("%Y-%m-%d %H:%M:%S")

    cursor = db.cursor()
    cursor.execute(data % date)
    time_delta = 0
    for user in cursor.fetchall():

        ext = QApi(phone=config.phone, token=config.token_qiwi)
        comment = ext.bill(comment=user[1])

        ext.run()
        time.sleep(1)
        if ext.check_info(comment):
            cursor.execute('update payment set status = 1 where user_id = %s' % user[0])
            db.commit()
        ext.close()
        time_delta+=1


    db.close()
    return time_delta



while True:
    try:
        max_time, tmp_time = 360, 0
        while tmp_time < max_time:
            tmp_time+=find('localhost', 'root', 'activeDB')
        time.sleep(3)
    except:
        time.sleep(5)
