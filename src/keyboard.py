# -*- coding: utf-8 -*-

import telebot
import config
import func
bot = telebot.TeleBot(config.token)

#Кнопки
class Keyboard:
    def __init__(self, bot):
        self.bot = bot
    def hide(self):
        markup = telebot.types.ReplyKeyboardRemove(True)
        return markup
    def menu(self):
        menu_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        menu_markup.row("В главное меню")
        return menu_markup

    def country(self):
        return func.create_keyboard(func.country())

    def state(self, call):
        return func.create_keyboard(func.state(call))

    def city(self, call):
        return func.create_keyboard(func.city(call))

    def our_choice(self, call):
        return func.create_keyboard(func.our_choice(call))

    def buy_menu(self):
        buy_markup = telebot.types.InlineKeyboardMarkup()
        buy_markup.add(telebot.types.InlineKeyboardButton(text = 'Выбрать страну', callback_data = 'country'))
        #buy_markup.add(telebot.types.InlineKeyboardButton(text = 'Выбрать область/штат', callback_data = 'state'))
        #buy_markup.add(telebot.types.InlineKeyboardButton(text = 'Выбрать город', callback_data = 'city'))
        return buy_markup

    def main_menu(self):
        menu_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        menu_markup.row("Купить vpn")
        return menu_markup
