import time,datetime
import utils
from core.QApiWallet import QApi


def cmp_time_status(delta=10):
    for val in utils.get_all():
        if datetime.datetime.strptime(str(val[4]),"%Y-%m-%d %H:%M:%S") + datetime.timedelta(minutes=delta) < datetime.datetime.now():
            utils.update_status_product(val[3],sign=0)
            utils.delete_payment(val[4], val[1])

def func():
    tmp = QApi(token = config.qiwitoken, phone = '+79998038494').payments
    for x in tmp['data']:
        if x['statusText'] == 'Success'  and x['type'] == 'IN':
            res = select_file_name(str(token[0]))[-1]
            price = select_price(res[0])[-1]
            if x['sum']['amount'] >= price:
                utils.update_payment(x['comment'])
                utils.update_status_product(val[3],sign=2)
            time.sleep(2)


while True:
    cmp_time_status()
    time.sleep(60)
#    if len(utils.get_all()) > 0:
#        func()
