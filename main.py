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


@bot.message_handler(func=lambda message: message.text in ['Курсы спортивного программирования', 'Курсы CTF',
                                                           '"Продлёнка Айтишника"', 'Вступление в СНО ВГУ', 'Назад'])
def simple_message_answer(message):
    if message.text == 'Курсы спортивного программирования':
        bot.send_message(message.chat.id, "Курсы спортивного программирования? А, эм... "
                                          "К сожалению в разработке бота не принимали участия представителя этого "
                                          "направления, все вопросы к ним")
    elif message.text == '"Продлёнка Айтишника"':
        bot.send_message(message.chat.id, "Ну этого когда матёрые програмисты котяры расссказывают студентам "
                                          "котятам как им ходить в ... С чем им предстоит столкнуться на работе по "
                                          "специальности. Все же выпускники ФКН будут работать по специальности?")
    elif message.text == 'Вступление в СНО ВГУ':
        bot.send_message(message.chat.id, "Вот если сделаешь нам пару тасков ...")
    elif message.text == 'Курсы CTF':
        bot.send_message(message.chat.id, 'Вместо 1000 слов, оть чат ТГ @vrnCTFCourses')
    elif message.text == 'Назад':
        start_place(message)


bot.polling(none_stop=True, interval=0)
