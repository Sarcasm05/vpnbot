from core.msq import Msq
import mysqldb
from config import database_name
import telebot
ef add_user(user_id):
    bd = Msq(database_name)
    bd.add_user(user_id)
    bd.close()

def autorisation(user_id):
    bd = Msq(database_name)
    if not bd.select_user(user_id):
        return 0

    return 1

def change_user_state(user_id, state):
    bd = Msq(database_name)
    bd.update_user_state(user_id, state)
    bd.close()



def create_keyboard(row):
    markup = telebot.types.InlineKeyboardMarkup()
    myset = set(row)
    for elem in myset:
        if type(elem[0]) != type(None) and len(elem[0])>0:
            markup.add(telebot.types.InlineKeyboardButton(text = elem[0][0], callback_data = elem[0][0]))
    markup.add(telebot.types.InlineKeyboardButton(text = "Return to main menu", callback_data = 'menu'))
    return markup


def select_user_state(user_id):
    bd = Msq(database_name)
    state = bd.select_user_state(str(user_id))
    bd.close()
    return state

def choice(user_id):
    bd = Msq(database_name)
    choice = bd.choice(user_id)
    bd.close()
    return choice
