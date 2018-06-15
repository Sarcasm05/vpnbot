import telebot
import config
import keyboard
import utils
from core.qiwi_wallet import push_qiwi_transaction
from Crypto.Hash import MD5, SHA256

import time
from core import WalletQiwi

import datetime
import MySQLdb


from utils import choice
from utils import add_user
from utils import autorisation
from utils import change_user_state
from utils import update_user_token
from utils import update_user_choice
from utils import update_user_payment_status
from utils import update select_user
from utils import create_keyboard
from utils import in_country
from utils import exist
from utils import our_choice
from utils import in_zip
from utils import in_city
from utils import in_state
from utils import city
from utils import state
from utils import country
from utils import select_namefile_none
from utils import select_user_state
from utils import select_user_token
from utils import select_user_choice
from utils import select_user_payment_status
from utils import add_user


bot = telebot.TeleBot(config.token)
keyboard = keyboard.Keyboard(bot)
QApi = WalletQiwi.QApi
ext = QApi(phone=config.phone, token=config.token_qiwi)

# Начало диалога
@bot.message_handler(commands=["start"])
def cmd_start(message):
    if autorisation(message.from_user.id):
        change_user_state(message.from_user.id, 0)
        bot.send_message(message.chat.id, "With this bot you can buy a vpn client", reply_markup = keyboard.buy_menu())
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
                    str(select_user_token(call.from_user.id))+" ,\nafter payment the bot within a few minutes will send you your vpn client and additional insturctions",reply_markup = keyboard.payment_menu())
#            push_qiwi_transaction(call.from_user.id, select_user_token(call.from_user.id) , 'to chto  bubral client')




        if select_user_state(call.from_user.id) == 2 and in_city(call.data):
            update_user_choice(call.from_user.id, select_namefile(call.data))

            #md5(a)[0:3]+sha256(a)[7:10]
            choice = select_user_choice(call.from_user.id)

            h = MD5.new()
            h.update(choice.encode('utf-8'))
            g = SHA256.new()
            g.update(choice.encode('utf-8'))
            token = h.hexdigest()[0:4] + g.hexdigest()[6:10]
            update_user_token(call.from_user.id, token)
            update_user_payment_status(call.from_user.id, 0)

            change_user_state(call.from_user.id, 4)

            push_qiwi_transaction(call.message.chat.id, select_user_token(call.from_user.id) , select_user_choice(call.from_user.id))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Choose a payment method :",reply_markup = keyboard.payment_menu())



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
                    str(select_user_token(call.from_user.id)), reply_markup = keyboard.payment_menu())


    #else:

    #    if len(tmp) > 2:
    #            bot.send_message(tmp, text='srabotalo')

if __name__ == "__main__":
    bot.polling(none_stop=True)
