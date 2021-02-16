import telebot
from datetime import datetime
import time

bot = telebot.TeleBot('1533518714:AAHEUE0GuFgo8RsMCZI6-CnAPmEEHWtH5gk')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(self, message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)
    self.remove_keyboard = True

@bot.message_handler(commands=['talk'])
def talk_message(message):
    bot.send_message(message.chat.id, text='Привет, давай пообщаемся?')

@bot.message_handler(commands=['horsemen'])
def horsemen_message(message):
    bot.send_message(message.chat.id, 'Это Конь ДИБ - а ты иди работай!')
    bot.send_photo(message.chat.id, 'https://kubnews.ru/upload/iblock/4e5/4e523d68c56d8710de2e2d5783d18a3a.jpg')
    bot.send_message(message.chat.id, 'Скорость, Сила, Эффективность - это Конь ДИБ')
    bot.send_photo(message.chat.id, 'https://static8.depositphotos.com/1001374/965/i/600/depositphotos_9652327-stock-photo-bay-horse-gallop.jpg')

#дежурные
sveta = 'Светлана' and 'светлана'
sergey = 'Сергей' and 'сергей'
yuri = 'Юрий' and 'юрий'
nikolay = 'Николай' and 'николай'
stopbot = 'остановить бота'
comment = 'добавить комментарий'
d = datetime.now()

@bot.message_handler(commands=['who'])
def stop_work(message):
     bot.send_message(message.chat.id, 'Дежурит - Света \n'
                                       'Дежурит - Юрий'
                                       '\n Дежурит - Николай'
                                       '\n Дежурит - Сергей')

@bot.message_handler(commands=['help'])
def stop_work(message):
     bot.send_message(message.chat.id, 'Список команд: \n /who - выводит дежурного(нет) \n '
                                       '/stopbot - останавливает бот(нет)')

@bot.message_handler(commands=['work'])
@bot.message_handler(content_types=['text'])
@bot.message_handler(commands=['stopbot'])
def start_work(message):
 while True:
  if message.text.lower() == 'сергей':
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Сергей \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Юрий \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Сергей \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Светлана \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Юрий \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Светлана \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Юрий \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Николай \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Светлана \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Николай \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Светлана \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Сергей \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Николай \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Сергей \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Николай \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Юрий \n День')
      time.sleep(43200)

  elif message.text.lower() == 'света':

      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Светлана \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Николай \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Светлана \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Сергей \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Николай \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Сергей \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Николай \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Юрий \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Сергей \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Юрий \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Сергей \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Светлана \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Юрий \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Светлана \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Юрий \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Николай \n День')
      time.sleep(43200)

  elif message.text.lower() == 'николай':

      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Николай \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Сергей \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Николай \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Юрий \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Сергей \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Юрий \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Сергей \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Светлана \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Юрий \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Светлана \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Юрий \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Николай \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Светлана \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Николай \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Светлана \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Сергей \n День')
      time.sleep(43200)
  elif message.text.lower() == 'юрий':

      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Юрий \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Светлана \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Юрий \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Николай \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Светлана \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Николай \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Светлана \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Сергей \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Николай \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Сергей \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Николай \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Юрий \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Сергей \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Юрий \n День')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Сергей \n Ночь')
      time.sleep(43200)
      bot.send_message(message.chat.id, d)
      bot.send_message(message.chat.id, 'Сейчас дежурит Светлана \n День')
      time.sleep(43200)
  elif message.text == 'stopbot':
   bot.send_message(message.chat.id, d)
   bot.send_message(message.chat.id, 'Остановка действия программы')
  break

#@bot.message_handler(commands=['stopbot'])
#def stop_work(message):
     #bot.send_message(message.chat.id, 'Остановка выполнения')
     #running = False



@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, хорошего дня!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, коллега')
    elif message.text.lower() == 'нет':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALD9WAWZ2piHUY1jtFznW7tE9taYHc_AAKEAgACVp29CmM4BwNuLcC6HgQ')
    elif message.text.lower() == 'конь':
        bot.send_photo(message.chat.id, 'https://newacropolis.org.ua/uploads/production/ckeditor/picture/data/1d8/16b/15-/1d816b15-e6d4-47f0-9e06-9294d1db9129/content.png')
    elif message.text.lower() == 'с днём рождения' and 'с днем рождения':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALD-mAWatISkeZpP5Boxi5oJXb5aKydAAKLAgACVp29Cve0YiYNjzvzHgQ')
    elif message.text.lower() == 'что ты такое?':
        bot.send_video(message.chat.id, 'https://youtu.be/gojmDEvjPR4')
    elif message.text.lower() == 'text':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALE5mAX0Y9cycgD3EehtWN2d4al6UqWAAKAAgACVp29CqCjII2WjOH2HgQ')




@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()