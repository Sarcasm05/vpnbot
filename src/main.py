import telebot
import config
import keyboard

 
bot = telebot.TeleBot(config.token)
keyboard = keyboard.Keyboard(bot)

# Начало диалога
@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id, "Стартовое окно, купи vpn уебок!", reply_markup = keyboard.main_menu())


@bot.message_handler(func=lambda mess: "Купить vpn" == mess.text, content_types=['text'])
def handle_text(message):
    bot.send_message(message.from_user.id, 'Выберите пункт меню : ', reply_markup=keyboard.buy_menu())


#обработчик коллбеков
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "country":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Выберите страну: ",reply_markup = keyboard.country())
        elif call.data == "state":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Выберите штат/область: ",reply_markup = keyboard.state())
        elif call.data == "city":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="Выберите город: ",reply_markup = keyboard.city())
        
  


if __name__ == "__main__":
    bot.polling(none_stop=True)	
