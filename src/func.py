# -*- coding: utf-8 -*-
import sqlite3
import config
import telebot
from SQLite import liter



def country():       
    bd = liter(config.database_name) 
    row = bd.select_country()
    bd.close()
    return row

def state():
    bd = liter(config.database_name) 
    row = bd.select_state()
    bd.close()
    return row

def city():
    bd = liter(config.database_name) 
    row = bd.select_city()
    bd.close()
    return row

def exist(call):
    bd = liter(config.database_name) 
    if len(bd.exist(call)) == 0:
        bd.close()
        return False
    else : 
        bd.close()
        return True



def create_keyboard(row):
    markup = telebot.types.InlineKeyboardMarkup()
    for elem in row :
        markup.add(telebot.types.InlineKeyboardButton(text = str(elem), callback_data = str(elem)))
    return markup