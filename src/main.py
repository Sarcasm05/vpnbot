# -*- coding: utf-8 -*-
import telebot
import config
import keyboard
import func
from Crypto.Hash import MD5, SHA256
bot = telebot.TeleBot(config.token)
keyboard = keyboard.Keyboard(bot)


# Начало диалога
@bot.message_handler(commands=["start"])
def cmd_start(message):
    if func.autorisation(message.from_user.id):
        func.change_user_state(message.from_user.id, 0)
        bot.send_message(message.chat.id, "With this bot you can buy a vpn client", reply_markup = keyboard.buy_menu())
    else:
        func.add_user(message.from_user.id)
        bot.send_message(message.chat.id, "With this bot you can buy a vpn client", reply_markup = keyboard.buy_menu())
        

@bot.message_handler(func=lambda mess: "Buy vpn" == mess.text, content_types=['text'])
def handle_text(message):
    bot.send_message(message.from_user.id, 'Select the menu item : ', reply_markup=keyboard.buy_menu())
    func.change_user_state(message.from_user.id, 0)




#обработчик коллбеков
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "country" and func.select_user_state(call.from_user.id) == 0 :
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Select country: ",reply_markup = keyboard.country())

        if func.select_user_state(call.from_user.id) == 0 and func.in_country(call.data):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Select district: ",reply_markup = keyboard.state(call.data))
            func.change_user_state(call.from_user.id, 1)

        if func.select_user_state(call.from_user.id) == 1 and func.in_state(call.data):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Select city: ",reply_markup = keyboard.city(call.data))
            func.change_user_state(call.from_user.id, 2)
        """
        if func.select_user_state(call.from_user.id) == 2 and func.in_city(call.data):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Выберите zip: ",reply_markup = keyboard.our_choice(call.data))
            func.change_user_state(call.from_user.id, 3)
        """
        if func.select_user_state(call.from_user.id) == 2 and func.in_city(call.data):
            func.update_user_choice(call.from_user.id, func.select_namefile(call.data))
            func.change_user_state(call.from_user.id, 4)
            #md5(a)[0:3]+sha256(a)[7:10]
            choice = func.select_user_choice(call.from_user.id)
            
            h = MD5.new()
            h.update(choice.encode('utf-8'))
            g = SHA256.new()
            g.update(choice.encode('utf-8'))
            token = h.hexdigest()[0:3] + g.hexdigest()[7:10]
            func.update_user_token(call.from_user.id, token)
            func.update_user_payment_status(call.from_user.id, 0)
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text = 'qiwi', callback_data = 'qiwi'))
            markup.add(telebot.types.InlineKeyboardButton(text = 'Back to the menu', callback_data = 'menu'))

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Choose a payment method :",reply_markup = markup)
        if func.select_user_state(call.from_user.id) == 4 and call.data == 'qiwi':
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text = 'Go to payment', url = 'https://qiwi.com/'))
            markup.add(telebot.types.InlineKeyboardButton(text = 'Back to the menu', callback_data = 'menu'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text = 'You choosed : ' + func.choice(call.from_user.id)+"\nPay for qiwi +79282765871 for $4 with a comment: " +
                    str(func.select_user_token(call.from_user.id))+" ,\nafter payment the bot within a few minutes will send you your vpn client and additional insturctions",reply_markup = markup)
        
        if call.data == 'menu':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Select the menu item : ', reply_markup = keyboard.buy_menu())
            func.change_user_state(call.from_user.id, 0)


        if call.data == 'account':
            choice = func.choice(call.from_user.id)
            if choice == 'null':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='You have not selected any vpn client to pay.', reply_markup = keyboard.menu())
            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='You choosed : ' + choice, reply_markup = keyboard.payment_menu())

if __name__ == "__main__":
    bot.polling(none_stop=True)
