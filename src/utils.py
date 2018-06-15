# -*- coding: utf-8 -*-
"""
    created by brdsky
"""

import sqlite3
from config import database_name
import telebot
from core.SQLite import Liter


def choice(user_id):
    bd = Liter(database_name)
    choice = bd.choice(user_id)
    bd.close()
    return choice

def add_user(user_id):
    bd = Liter(database_name)
    bd.add_user(user_id)
    bd.close()

def autorisation(user_id):
    bd = Liter(database_name)
    if not bd.select_user(user_id):
        return 0
    else :
        return 1

def change_user_state(user_id, state):
    bd = Liter(database_name)
    bd.update_user_state(user_id, state)
    bd.close()

def update_user_choice(user_id, choice):
    bd = Liter(database_name)
    bd.update_user_choice(user_id, choice)
    bd.close()

def update_user_token(user_id, token):
    bd = Liter(database_name)
    bd.update_user_token(user_id, token)
    bd.close()

def update_user_payment_status(user_id, status):
    bd = Liter(database_name)
    bd.update_user_payment_status(user_id, status)
    bd.close()

def select_user_state(user_id):
    bd = Liter(database_name)
    state = bd.select_user_state(user_id)
    bd.close()
    return state

def select_user_choice(user_id):
    bd = Liter(database_name)
    choice = bd.select_user_choice(user_id)
    bd.close()
    return choice

def select_user_token(user_id):
    bd = Liter(database_name)
    token = bd.select_user_token(user_id)
    bd.close()
    return token

def select_user_payment_status(user_id):
    bd = Liter(database_name)
    status = bd.select_user_payment_status(user_id)
    bd.close()
    return status

def select_namefile(choice):
    bd = Liter(database_name)
    vpn = bd.select_namefile(choice)
    bd.close()
    return vpn

def select_namefile_none(choice):
    bd = Liter(database_name)
    vpn = bd.select_namefile_none(choice)
    bd.close()
    return vpn

def country():
    bd = Liter(database_name)
    row = bd.select_country()
    bd.close()
    return row

def state(country):
    bd = Liter(database_name)
    row = bd.select_state(country)
    bd.close()
    return row

def city(state):
    bd = Liter(database_name)
    row = bd.select_city(state)
    bd.close()
    return row

def our_choice(city):
    bd = Liter(database_name)
    row = bd.our_choice(city)
    bd.close()
    return row

def exist(call):
    bd = Liter(database_name)
    if len(bd.exist(call)) == 0:
        bd.close()
        return False
    else :
        bd.close()
        return True

def in_country(call):
    bd = Liter(database_name)
    sign = 1
    if not bd.in_country(call):
        sign = 0
    bd.close()

    return sign

def in_state(call):
    bd = Liter(database_name)
    if not bd.in_state(call):
        bd.close()
        return 0
    else :
        bd.close()
        return 1

def in_city(call):
    bd = Liter(database_name)
    if not bd.in_city(call):
        bd.close()
        return 0
    else :
        bd.close()
        return 1

def in_zip(call):
    bd = Liter(database_name)
    if not bd.in_zip(call):
        bd.close()
        return 0
    else :
        bd.close()
        return 1

def create_keyboard(row):
    markup = telebot.types.InlineKeyboardMarkup()
    myset = set(row)
    for elem in myset :
        if type(elem[0]) != type(None) and len(elem[0])>0:
            markup.add(telebot.types.InlineKeyboardButton(text = elem[0], callback_data = elem[0]))
    markup.add(telebot.types.InlineKeyboardButton(text = "Return to main menu", callback_data = 'menu'))
    return markup
