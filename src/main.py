import telebot
import config
import keyboard

from core.qiwi_wallet import push_qiwi_transaction
from Crypto.Hash import MD5, SHA256

import time
from core import WalletQiwi

import datetime
import MySQLdb


from func import *


bot = telebot.TeleBot(config.token)
keyboard = keyboard.Keyboard(bot)
QApi = WalletQiwi.QApi
ext = QApi(phone=config.phone, token=config.token_qiwi)

# Начало диалога
@bot.message_handler(commands=["start"])
def cmd_start(message):
    if autorisation(message.from_user.id):
        change_user_state(message.from_user.id, 0)
    else:
        add_user(message.from_user.id)
    bot.send_message(message.chat.id, "With this bot you can buy a vpn client", reply_markup = keyboard.buy_menu())


@bot.message_handler(func=lambda mess: "Buy vpn" == mess.text, content_types=['text'])
def handle_text(message):
    bot.send_message(message.from_user.id, 'Select the menu item : ', reply_markup=keyboard.buy_menu())
    change_user_state(message.from_user.id, 0)



#обработчик коллбеков
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global ext
    if call.message:

        if select_user_state(call.from_user.id) == 4 and call.data == 'qiwi':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text = 'You choosed : ' + choice(call.from_user.id)+"\nPay for qiwi +79998038494 for 10rub with a comment: " +
                    select_user_token(call.from_user.id)+" ,\nafter payment the bot within a few minutes will send you your vpn client and additional insturctions",reply_markup = keyboard.payment_menu())
#            push_qiwi_transaction(call.from_user.id, select_user_token(call.from_user.id) , 'to chto  bubral client')





        if call.data == 'menu':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Select the menu item : ', reply_markup = keyboard.buy_menu())
            change_user_state(call.from_user.id, 0)

        if select_user_state(call.from_user.id) == 1 and in_state(call.data):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Select city: ",reply_markup = keyboard.city(call.data))
            change_user_state(call.from_user.id, 2)

        if select_user_state(call.from_user.id) == 0 and in_country(call.data):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Select district: ",reply_markup = keyboard.state(call.data))
            change_user_state(call.from_user.id, 1)

        if call.data == "country" and select_user_state(call.from_user.id) == 0 :
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Select country: ",reply_markup = keyboard.country())




        """
        if select_user_state(call.from_user.id) == 2 and in_city(call.data):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Выберите zip: ",reply_markup = keyboard.our_choice(call.data))
            change_user_state(call.from_user.id, 3)
        """



        if call.data == 'account':
            choice = choice(call.from_user.id)
            if choice == 'null':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='You have not selected any vpn client to pay.', reply_markup = keyboard.menu())
            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='You choosed : ' + choice + "\nPay for qiwi +79282765871 for $4 with a comment: " +
                    select_user_token(call.from_user.id), reply_markup = keyboard.payment_menu())


    #else:

    #    if len(tmp) > 2:
    #            bot.send_message(tmp, text='srabotalo')

if __name__ == "__main__":
    bot.polling(none_stop=True)
