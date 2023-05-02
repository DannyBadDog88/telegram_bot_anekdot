import requests
import random
import telebot
from bs4 import BeautifulSoup as b

URL = 'https://www.anekdot.ru/last/anekdot/'
API_KEY = '6074612130:AAHK_aRZ7bQTZQdUuO0FpiH6Zh5Q2oayDAM'

def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_ = 'text')
    return[c.text for c in anekdots]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['начать'])

def hello(message):
    bot.send_message(message.chat.id, 'Хай! Меня зовут Дэнни бот, кидай цифру от 1 до 9, получишь анекдот')

@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Введи цифру от 1 до 9')    
bot.polling()    