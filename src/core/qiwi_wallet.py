"""

create table payment
(
    payment_id INT NOT NULL AUTO_INCREMENT,
    user_id VARCHAR(32) NOT NULL,
    token VARCHAR(8) NOT NULL,
    name_ovpn VARCHAR(32) NOT NULL,
    datatime DATETIME,
    status tinyint(1) default NULL,
    PRIMARY KEY (payment_id)
);

insert into payment(payment_id, user_id, token, name_ovpn, datatime)
            values (NULL, '32123', 'sado21sd', 'ovpn_91.101.2.13.ovpn', '2018-05-31 01:30:32');

insert into payment(payment_id, user_id, token, name_ovpn, datatime)
            values (NULL, '72323', 'Asdo21sd', 'ovpn_9.121.4.33.ovpn', '2018-05-31 03:30:32');

token - уникальный код, который пользователь должен приложить, как комментарий к платежу
name_ovpn - название *.ovpn файла, который он получит в случае успешной оплаты
status - if status == 1: поступил платеж. вот именно на него тебе и нужен callback
"""
import MySQLdb
import datetime


def push_qiwi_transaction(user_id, token_auth, file_ovpn):
    private_sql_req = 'insert into payment(payment_id, user_id, token, name_ovpn, datatime) values(NULL, \'%s\', \'%s\', \'%s\', \'%s\');'

    try:
        db = MySQLdb.connect(host='localhost',user='root', db='activeDB')
    except:
        print('mysql connect error')


    with  db as cursor:
        cursor.execute(private_sql_req % (user_id, token_auth, file_ovpn, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


    db.commit()
    db.close()
