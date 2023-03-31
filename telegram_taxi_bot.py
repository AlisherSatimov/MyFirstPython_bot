from telebot import TeleBot, types
import requests
from users import User
TOKEN = '6267766884:AAH2pWuNnT3f_QRB9uEOF1F4LSbljTR0s24'

bot = TeleBot(TOKEN)
users = []

@bot.message_handler(func=lambda message:message.text=="salom")
def salom(message):
    bot.send_message(message.chat.id, text="Volaykum Assalom ishlar yaxshimi 🙋‍♂️")

@bot.message_handler(commands=['start'])

def boshlash(message):
    tugmalar = types.ReplyKeyboardMarkup(True)
    tugma1 = types.KeyboardButton(text="Kantakt ulashish", request_contact=True)
    tugma2 = types.KeyboardButton("Lakatsiya ulashish", request_location=True)
    tugmalar.row(tugma1)
    tugmalar.row(tugma2)

    ulashish = bot.send_message(message.chat.id, "Ulashish 👇", reply_markup=tugmalar)
    bot.register_next_step_handler(ulashish, ruyxatlar)

def ruyxatlar(message):
    del_tugmalar = types.ReplyKeyboardRemove()
    obj = User(message.chat.id, message.chat.first_name, message.id-1, message.id)
    users.append(obj)

bot.polling()


