import time, datetime
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

now = datetime.datetime.now()

def loopAction(msg):
    content_type, chat_type, user_id = telepot.glance(msg)

    keyboard = ReplyKeyboardMarkup(keyboard = [
        [KeyboardButton(text = "/on"), KeyboardButton(text = "/off")],[ KeyboardButton(text = "/retakepicture"),
         KeyboardButton(text = "/mrjonathan")]
        ], one_time_keyboard = True
    )
    
    if content_type == 'text':
        command = msg['text']
        print(user_id)

        if command == "/mrsanyong":
            telegram_bot.sendMessage(user_id, "Hi Sanyong")
        elif command == "/mrjonathan":
            telegram_bot.sendMessage(user_id, "ITS JON CENA!!!!!!!!!!!!!!!!!")
            telegram_bot.sendPhoto(user_id, photo = "https://upload.wikimedia.org/wikipedia/commons/7/77/John_Cena_May_2016.jpg") 
        elif command == "/reset":

        elif command == "/bot":
            telegram_bot.sendMessage(user_id, "Please select an option", reply_markup = keyboard, )
                                     

telegram_bot = telepot.Bot('382774272:AAHvT_9m9IW3u5q0NJM5U389RMqzStID22o')

MessageLoop(telegram_bot, loopAction).run_as_thread()
print('Listening...')

while 1:
    time.sleep(10)
