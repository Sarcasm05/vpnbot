from core.FindBranch import AdoptBranch
import telebot
def add_user(user_id):
    with AdoptBranch() as cur:
        cur.execute(AdoptBranch.add_user(user_id))

def autorisation(user_id):
    with AdoptBranch() as bd:
        if not bd.execute(AdoptBranch.select_user(user_id)):
            return 0
        return 1

def change_user_state(user_id, state):
    with AdoptBranch() as bd:
        bd.execute(AdoptBranch.update_user_state(user_id, state))


def select_user_state(user_id):
    with AdoptBranch() as bd:
        bd.execute(AdoptBranch.select_user_state(user_id))
        return bd.fetchone()[0]

def get_token(user_id):
    with AdoptBranch() as bd:
        bd.execute(AdoptBranch.get_token(user_id))
        return bd.fetchall()

def country():
    with AdoptBranch() as bd:
        bd.execute(AdoptBranch.select_country())
        return bd.fetchall()

def state(country):
    with AdoptBranch() as bd:
        bd.execute(AdoptBranch.select_state(country))
        return bd.fetchall()

def city(state):
    with AdoptBranch() as bd:
        bd.execute(AdoptBranch.select_city(state))

        return bd.fetchall()

def our_choice(city):
    with AdoptBranch() as bd:
        bd.execute(AdoptBranch.our_choice(city))

        return bd.fetchall()

def exist(call):
    with AdoptBranch() as bd:
        if len(bd.exist(call)) == 0:

            return False
        else :

            return True

def in_country(call):
    with AdoptBranch() as bd:
        sign = 1
        if not bd.execute(AdoptBranch.in_country(call)):
            sign = 0


        return sign

def in_state(call):
    with AdoptBranch() as bd:
        if not bd.execute(AdoptBranch.in_state(call)):

            return 0
        else :

            return 1

def in_city(call):
    with AdoptBranch() as bd:
        if not bd.execute(AdoptBranch.in_city(call)):

            return 0
        else :

            return 1

def add_payment(call):
    with AdoptBranch() as bd:
        bd.execute(AdoptBranch.in_zip(call))

def get_filename(val):
    with AdoptBranch() as bd:
        bd.execute(AdoptBranch.get_filename(val))
        return bd.fetchone()[0]

def add_pay(token, user_id, file_name, data_req, status):
    with AdoptBranch() as bd:
        bd.execute(AdoptBranch.add_pay(token, user_id, file_name, data_req, status))

def get_payments(user_id):
    with AdoptBranch() as bd:
        bd.execute(AdoptBranch.get_payments(user_id))
        return bd.fetchall()


def create_keyboard(row):
    markup = telebot.types.InlineKeyboardMarkup()

    myset = set(row)

    #print(myset)
    for elem in myset:
        if type(elem[0]) != type(None) and len(elem[0])>0:
            markup.add(telebot.types.InlineKeyboardButton(text = elem[0], callback_data = elem[0]))
    #markup.add(telebot.types.InlineKeyboardButton(text = "Return to main menu", callback_data = 'menu'))
    return markup
