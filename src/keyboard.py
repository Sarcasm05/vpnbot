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
        buy_markup.add(telebot.types.InlineKeyboardButton(text = 'Select Country', callback_data = 'country'))
        buy_markup.add(telebot.types.InlineKeyboardButton(text = 'My choice', callback_data = 'account'))
        buy_markup.add(telebot.types.InlineKeyboardButton(text = 'Technical support', url = 'telegram.me/brdsky'))
        return buy_markup

    def menu(self):
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text = 'Back to the menu', callback_data = 'menu'))
        return markup

    def payment_menu(self):
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text = 'Go to payment', url = 'https://qiwi.com/'))
        markup.add(telebot.types.InlineKeyboardButton(text = 'Back to the menu', callback_data = 'menu'))
        return markup
