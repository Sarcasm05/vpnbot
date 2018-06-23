import MySQLdb
import telebot
import config
import keyboard

from core.FindBranch import AdoptBranch
from utils import *



bot = telebot.TeleBot(config.token)
keyboard = keyboard.Keyboard(bot)


# Начало диалога
@bot.message_handler(commands=["start"])
def cmd_start(message):

    if autorisation(message.from_user.id):
        change_user_state(message.from_user.id, 0)
    else:
        add_user(message.from_user.id)

    bot.send_message(message.chat.id, "With this bot you can buy a vpn client", reply_markup = keyboard.buy_menu())

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:

        if call.data == 'menu':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Select the menu item : ', reply_markup = keyboard.buy_menu())
            change_user_state(call.from_user.id, 0)

        if select_user_state(call.from_user.id) == 1 and in_state(call.data):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Select city: ",reply_markup = keyboard.city(call.data))
            change_user_state(call.from_user.id, 2)


        if select_user_state(call.from_user.id) == 0 and in_country(call.data):
        #    print(call.data)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Select district: ",reply_markup = keyboard.state(call.data))

            change_user_state(call.from_user.id, 1)

        if call.data == "country" and select_user_state(call.from_user.id) == 0 :
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Select country: ",reply_markup = keyboard.country())

    #    if select_user_state(call.from_user.id) == 2:




if __name__ == "__main__":
    bot.polling(none_stop=True)
