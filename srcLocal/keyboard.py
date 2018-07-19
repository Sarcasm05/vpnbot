# -*- coding: utf-8 -*-

import telebot
import config
import utils

bot = telebot.TeleBot(config.token)

#Кнопки
class Keyboard:
    def __init__(self, bot):
        self.bot = bot
    def hide(self):
        markup = telebot.types.ReplyKeyboardMarkup(True, True)
        return markup

    def country(self):
        return utils.create_keyboard(utils.country())

    def state(self, call):
        return utils.create_keyboard(utils.state(call))

    def city(self, call):
        return utils.create_keyboard(utils.city(call))

    def our_choice(self, call):
        return utils.create_keyboard(utils.our_choice(call))


    def buy_menu(self):
        buy_markup = telebot.types.InlineKeyboardMarkup()
        buy_markup.add(telebot.types.InlineKeyboardButton(text = 'Select Country', callback_data = 'country'))
        return buy_markup

    def menu(self):
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text = 'Back to the menu', callback_data = 'menu'))
        return markup

    def payment_method(self):
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text = 'qiwi', callback_data = 'qiwi'))
        markup.add(telebot.types.InlineKeyboardButton(text = 'bitcoin', callback_data = 'bitcoin'))
        return markup

    def payment_menu(self):
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text = 'Go to payment', url = 'https://qiwi.com/'))
        #markup.add(telebot.types.InlineKeyboardButton(text = 'Back to the menu', callback_data = 'menu'))
        return markup

    def support(self):
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text = 'Support', url = 'https://t.me/brdsky'))
        return markup

    def down_menu(self):
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row(config.byeVPN, config.myPurchase)
        markup.row(config.techSupport)
        return markup

    def bye_menu(self):
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row(config.findByZip, config.selectManual)
        markup.row(config.backToMenu)
        return markup
    def back_menu(self):
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.OneTimeKeyboard = True
        markup.row(config.backToMenu)
