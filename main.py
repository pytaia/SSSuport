import telebot
from telebot import types
from PIL import Image
import io
from decoder import stegano

bot = telebot.TeleBot('7921804902:AAEte7WriDkKjmHAEB95utVGU61KmlBGxZQ')


#
@bot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document',
                                    'location', 'contact', 'sticker'])
def photo_handle(message):
    if ".png" in message.document.file_name:
        photo = message.document
        file_info = bot.get_file(photo.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        bot.send_message(message.chat.id, stegano(Image.open(io.BytesIO(downloaded_file))))
    else:
        bot.send_message(message.chat.id, "Обработка данного типа данных не поддерживается сейчас.")


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


@bot.message_handler(func=lambda message: message.text == "Что такое CTF")
def ctf_info(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Steganography'), types.KeyboardButton('WEB'), types.KeyboardButton('OSINT'),
               types.KeyboardButton('Reverse'), types.KeyboardButton('Cryptography'),
               types.KeyboardButton('Forensic'), types.KeyboardButton('Назад'))

    bot.send_message(message.chat.id, "Захват флага (англ. Capture the Flag или англ. CTF) в компьютерной безопасности "
                                      "— это упражнение, в котором «флаги» тайно прячутся в преднамеренно "
                                      "уязвимых программах или веб-сайтах. (взято с Википедии, а больше мы ничего и "
                                      "не знаем, крч вот чат @vrnCTFCourses)\n"
                                      "Выберите интересующую вас категорию заданий",
                     reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ['Steganography', 'WEB', 'OSINT', 'Reverse',
                                                           'Cryptography', 'Forensic', 'Назад'])
def ctf_task_category_info(message):
    if message.text == 'Steganography':
        bot.send_message(message.chat.id,
                         "Steganography (Стеганография) -  практика сокрытия сообщения, файла или информации "
                         "внутри других несекретных данных или носителя, таких как изображение, "
                         "аудиофайл или текст, таким образом, чтобы существование этих данных было скрыто.")
    elif message.text == 'OSINT':
        # Жирная подсказка куда надо дальше двигаться что бы получить флаг
        # Но можно дать ссылку на репозиторий в раделе OSINT чата Курсы CTF, просто поменять немного ответы бота
        # Участников нагнать заодно)
        bot.send_message(message.chat.id,
                         "OSINT (Поиск информации в открытых источниках) Поиск, выбор и сбор информации из "
                         "общедоступных источников, а также её анализ и систематизацию. Анализ данных из проектов "
                         "в Github, как часть Open Source разработки тоже можно считать частью OSINT, код "
                         "этого бота также представлен на Github (pytaia/SSSuport)")
    elif message.text == 'WEB':
        bot.send_message(message.chat.id,
                         "Web (Уязвимости веб-приложений, атака на веб-приложения) \n По больше части в "
                         "заданиях вам даётся адрес сайта, который нужно 'поломать' с помощью уязвимости. "
                         "Часто, на различных простых CTF'ах задания бывают просто на знание "
                         "устройства Веб-приложений.")
    elif message.text == 'Reverse':
        bot.send_message(message.chat.id,
                         'Reverse (обратная разработка) \n Исследование бинарных файлов (программ) без '
                         'исходных кодов и изучение работы различных редких архитектур.')
    elif message.text == 'Cryptography':
        bot.send_message(message.chat.id, 'Cryptography (криптография) Задания на криптографические алгоритмы. Бывают '
                                          'задания как на старинные алгоритмы, так и на современные.')
    elif message.text == 'Forensic':
        bot.send_message(message.chat.id, 'Forensic (компьютерная криминалистика) Задания посвящённые компьютерной '
                                          'криминалистики. В данную тематику входит: исследование различных дампов '
                                          '(сетевых, памяти и прочее), восстановление архивов.')
    else:
        start_place(message)


@bot.message_handler(func=lambda message: message.text == 'О VRN-CTF')
def vrn_ctf_info(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Материалы для подготовки'), types.KeyboardButton('Дата, время, место проведения'),
               types.KeyboardButton('Дают ли за победу разряд по ИБ?'), types.KeyboardButton('Назад'))

    bot.send_message(message.chat.id, "VRN-CTF - Первенство города Воронежа по спортивному программированию и "
                                      "компьютерной безопасности среди школьников и студентов.", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ['Материалы для подготовки', 'Дата, время, место проведения',
                                                           'Дают ли за победу разряд по ИБ?', 'Назад'])
def vrn_ctf_category_info(message):
    if message.text == 'Материалы для подготовки':
        bot.send_message(message.chat.id, "А эм, где то они были, надо поискать")
    elif message.text == 'Дата, время, место проведения':
        bot.send_message(message.chat.id, "В субботу весной")
    elif message.text == 'Дают ли за победу разряд по ИБ?':
        bot.send_message(message.chat.id, "Хехе Наивный чукотский школьник")
    else:
        start_place(message)


bot.polling(none_stop=True, interval=0)
