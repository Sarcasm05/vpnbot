"""
    будет это отдельным процессом или нет, я еще не решил.
"""

from core import WalletQiwi.QApi


token = ""
phone = ""

ext = QApi(token=token, phone=phone)


print(ext.payments)
