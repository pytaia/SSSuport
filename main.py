import telebot
from telebot import types

bot = telebot.TeleBot('7921804902:AAEte7WriDkKjmHAEB95utVGU61KmlBGxZQ')


@bot.message_handler(content_types=['document', 'video', 'photo'])
def handle_document(message):
    bot.send_message(message.chat.id, f"{message.document.file_name.end} файлы не поддерживаются. "
                                      f"Вы ошиблись разделом заданий )")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Я бот SSSupport (Student scientific society - Научного общества '
                                      'студентов) создан для помощи студентам и школьникам интересующимся '
                                      'деятельностью научного общества в получении ответов на их глупые вопросы.')
    start_place(message)


def start_place(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('О VRN-CTF'), types.KeyboardButton('Что такое CTF'),
               types.KeyboardButton('Курсы CTF'),
               types.KeyboardButton('Курсы спортивного программирования'),
               types.KeyboardButton('"Продлёнка Айтишника"'),
               types.KeyboardButton('Вступление в СНО ВГУ'))
    bot.send_message(message.chat.id, 'Выберете интересующий вас раздел', reply_markup=markup)


bot.polling(none_stop=True, interval=0)
