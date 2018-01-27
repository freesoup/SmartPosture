import time, datetime
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from server import requestTakePic
from server import requestNewUser

now = datetime.datetime.now()

cameraId = 0

def loopAction(msg):
    global cameraId
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
                data = {"calibrate":False, "image":False, "seat_exceeded":False, "timer":0}
                requestNewUser(str(user_id) + "," + cameraId, data)
            else:
                telegram_bot.sendMessage(user_id, "Camera ID verification error")
        #to reset reference image
        elif commandls[0] == "/calibrate":
            if cameraId!=0:
                requestTakePic(str(user_id) + "," + cameraId)
                #run Jackie's script to ping firebase
            else:
                telegram_bot.sendMessage(user_id, "no camera")
        #keyboard setting
        elif commandls[0] == "/bot":
            telegram_bot.sendMessage(user_id, "Please select an option", reply_markup = keyboard, )
                                     

telegram_bot = telepot.Bot('382774272:AAHvT_9m9IW3u5q0NJM5U389RMqzStID22o')

MessageLoop(telegram_bot, loopAction).run_as_thread()
print('Listening...')

while 1:
    time.sleep(10)
