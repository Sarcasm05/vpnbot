import telebot
import config
import keyboard
import func
 
bot = telebot.TeleBot(config.token)
keyboard = keyboard.Keyboard(bot)

# Начало диалога
@bot.message_handler(commands=["start"])
def cmd_start(message):
    if func.autorisation(message.from_user.id):
        func.change_user_state(message.from_user.id, 0)
        bot.send_message(message.chat.id, "Стартовое окно, купи vpn уебок!", reply_markup = keyboard.main_menu())
    else:
        func.add_user(message.from_user.id)
        bot.send_message(message.chat.id, "Стартовое окно, купи vpn уебок!", reply_markup = keyboard.main_menu())


@bot.message_handler(func=lambda mess: "Купить vpn" == mess.text, content_types=['text'])
def handle_text(message):
    bot.send_message(message.from_user.id, 'Выберите пункт меню : ', reply_markup=keyboard.buy_menu())
    func.change_user_state(message.from_user.id, 0)



#обработчик коллбеков
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if (call.data == "country" and func.select_user_state(call.from_user.id) == 0 ):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Выберите страну: ",reply_markup = keyboard.country())
        
        if func.select_user_state(call.from_user.id) == 0 and func.in_country(call.data):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Выберите штат: ",reply_markup = keyboard.state(call.data))
            func.change_user_state(call.from_user.id, 1)

        if func.select_user_state(call.from_user.id) == 1 and func.in_state(call.data):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Выберите город: ",reply_markup = keyboard.city(call.data))
            func.change_user_state(call.from_user.id, 2)

        if func.select_user_state(call.from_user.id) == 2 and func.in_city(call.data):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Выберите zip: ",reply_markup = keyboard.our_choice(call.data))
            func.change_user_state(call.from_user.id, 3)

        if func.select_user_state(call.from_user.id) == 3 and func.in_zip(call.data):
            func.update_user_choice(call.from_user.id, call.data)
            func.change_user_state(call.from_user.id, 4)
            vpn = func.select_vpn(call.data)
            string = ""
            for word in vpn:
                string += str(word) + " "
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Выш выбор \n" + string + "\nВыберите cпособ оплаты :\nu324iuy23pu4p23u4y23\n 23784623478643284 ")            
        if func.select_user_state(call.from_user.id) == 4:
            pass
  


if __name__ == "__main__":
    bot.polling(none_stop=True)	
