import time, datetime
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
import server.py

now = datetime.datetime.now()


def loopAction(msg):
    content_type, chat_type, user_id = telepot.glance(msg)

    keyboard = ReplyKeyboardMarkup(keyboard = 
        [KeyboardButton(text = "/setup"), KeyboardButton(text = "/calibrate")
        ], one_time_keyboard = True, resize_keyboard = True
    )
    
    if content_type == 'text':
        command = msg['text']
        commandls =[]
        print(user_id)

        #splitting to setup camera number
        commandls = command.split()

        #startup message with prompt for camera id
        if commandls[0] == "/start":
            telegram_bot.sendMessage(user_id, "To calibrate: /setup CameraNum")
        elif commandls[0] == "/setup":
            #assign camera id to firebase 
            cameraId = commandls[1]
            #verify if cameraId contains all numbers
            if cameraId.isdigit():
                telegram_bot.sendMessage(user_id, "Camera ID verified")
            else:
                telegram_bot.sendMessage(user_id, "Camera ID verification error")
        #to reset reference image
        elif commandls[0] == "/calibrate":
            requestTakePhoto(user_id + "," + cameraId)
            #run Jackie's script to ping firebase
        #keyboard setting
        else command[0] == "/bot":
            telegram_bot.sendMessage(user_id, "Please select an option", reply_markup = keyboard, )
                                     

telegram_bot = telepot.Bot('382774272:AAHvT_9m9IW3u5q0NJM5U389RMqzStID22o')

MessageLoop(telegram_bot, loopAction).run_as_thread()
print('Listening...')

while 1:
    time.sleep(10)
