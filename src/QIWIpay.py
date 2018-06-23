import MySQLdb
from core.qiwiwallet import QApi
import time
import config

def func():
    q = QApi(token = config.qiwitoken, phone = '+79998038494')
    tmp =  q.payments
    print(tmp)
    for x in tmp['data']:
        if x['statusText'] == 'Success'  and x['type'] == 'IN' and x['sum']['amount'] > 1:
            tmp = x['comment']
            print(tmp)
            connection =  MySQLdb.connect(host='localhost',user='root', db='activeDB')
            cursor = connection.cursor()
            cursor.execute('update Payment set  status = 1 WHERE  token = \'%s\'' % (tmp))
            connection.commit()
            connection.close()
            time.sleep(2)



while True:
    time.sleep(360)
    func()
