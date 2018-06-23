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

if __name__ == "__main__":
    bot.polling(none_stop=True)
