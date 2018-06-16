import telebot
import config
import keyboard


import datetime
import MySQLdb
import time

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

#            push_qiwi_transaction(call.from_user.id, select_user_token(call.from_user.id) , 'to chto  bubral client')



        if call.data == 'menu':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Select the menu item : ', reply_markup = keyboard.buy_menu())
            change_user_state(call.from_user.id, 0)
"""
        if select_user_state(call.from_user.id) == 0 and in_country(call.data):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Select district: ",reply_markup = keyboard.state(call.data))
            change_user_state(call.from_user.id, 1)

        if select_user_state(call.from_user.id) == 1 and in_state(call.data):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Select city: ",reply_markup = keyboard.city(call.data))
            change_user_state(call.from_user.id, 2)

"""

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
