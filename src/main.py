import MySQLdb
import telebot
import config
import keyboard
import time
import datetime
from core.FindBranch import AdoptBranch
from utils import *
import hashlib



bot = telebot.TeleBot(config.token)
keyboard = keyboard.Keyboard(bot)


# Начало диалога
@bot.message_handler(commands=["start"])
def cmd_start(message):

    if autorisation(message.from_user.id):
        change_user_state(message.from_user.id, 0)
    else:
        add_user(message.from_user.id)

    bot.send_message(message.chat.id, "With this bot you can buy a vpn client", reply_markup = keyboard.down_menu())


@bot.message_handler(func=lambda mess: "buy vpn" == mess.text, content_types=['text'])
def handle_text(message):
    change_user_state(message.from_user.id, 0)
    bot.send_message(message.from_user.id, 'Select country: ', reply_markup=keyboard.country())
@bot.message_handler(func=lambda mess: "find by zip code" == mess.text, content_types=['text'])
def handle_text(message):
    bot.send_message(message.from_user.id, 'enter zip code ')
    change_user_state(message.from_user.id, 5)


@bot.message_handler(func=lambda mess:  select_user_state(mess.from_user.id) == 5, content_types=['text'])
def handle_text(message):
    if str(message.text) in config.zip_arr :
        bot.send_message(message.from_user.id, "This zip code is on sale, for purchase, contact the support")
    else:
        bot.send_message(message.from_user.id, "sorry, but we don't have this zip_code")

@bot.message_handler(func=lambda mess: "my purchases" == mess.text, content_types=['text'])
def handle_text(message):
#    change_user_state(message.from_user.id, 0)
    data = get_payments(message.from_user.id)
    bot.send_message(message.from_user.id, 'All your purchases are valid 3 months')
    arr = list()
    for msg in data:
        arr.append(msg[3])


    for msg in set(arr):
        with open('/root/vpnbot/resources/root/%s' % msg) as fileObj:
            pair = get_login_pass(msg)[0]
            bot.send_document(message.from_user.id, fileObj, caption='login %s  password %s' %(pair[0], pair[1]))



@bot.message_handler(func=lambda mess: "technical support" == mess.text, content_types=['text'])
def handle_text(message):
    bot.send_message(message.from_user.id, config.technical_sup_str, reply_markup = keyboard.support())

@bot.message_handler(func=lambda mess: "donate" == mess.text, content_types=['text'])
def handle_text(message):
    change_user_state(message.from_user.id, 0)
    bot.send_message(message.from_user.id, config.donate + " - our bitcoin adress")



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if select_user_state(call.from_user.id) == 1 and in_state(call.data):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Select city: ",reply_markup = keyboard.city(call.data))
            change_user_state(call.from_user.id, 2)

        if select_user_state(call.from_user.id) == 0 and in_country(call.data):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Select district: ",reply_markup = keyboard.state(call.data))
            change_user_state(call.from_user.id, 1)


        if select_user_state(call.from_user.id) == 2 and in_city(call.data):

            timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            tmp = get_filename(call.data)
            token = hashlib.md5((str(call.from_user.id)  +  hashlib.md5(tmp.encode('utf-8')).hexdigest()[5:14]).encode('utf-8')).hexdigest()
            if len(cmp_token(token[5:11])) < 1:
                add_pay(token[5:11], call.from_user.id, tmp, timestamp, 0)
                change_user_state(call.from_user.id, 3)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                    text="Select pay method: ",reply_markup = keyboard.payment_method())


            else:
                bot.send_message(call.from_user.id, 'sorry, but the product was paid for')
                change_user_state(call.from_user.id, 0)


        if select_user_state(call.from_user.id) == 3 and call.data == 'qiwi':
            change_user_state(call.from_user.id, 4)
            token = get_token(call.from_user.id)[-1]
            bot.send_message(call.from_user.id, config.str_payment % (token[0], '+79998038494'))


        if select_user_state(call.from_user.id) == 3 and call.data == 'bitcoin':
            bot.send_message(call.from_user.id,"please, write to technical support")


if __name__ == "__main__":
    bot.polling(none_stop=True)
