import pyrebase
import _thread
import telepot

db = None
my_stream =None
userID = None
cameraID = None
telebot = None

def requestTakePic(childName):
    global db
    config = getConfig()

    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    #retrieve userid from auth token

    additional_claims = {
	  'premiumAccount': True
	}
    
    token = auth.create_custom_token("test", additional_claims)
    user = auth.sign_in_with_custom_token(token)
    uid = user['idToken']   
    
    db = firebase.database()

    db.child("users").child(childName).update({"calibrate":True}, uid)

def requestNewUser(childName, data):
    global db
    config = getConfig()

    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()

    additional_claims = {
	'premiumAccount': True
    }
        
    token = auth.create_custom_token("test", additional_claims)
    user = auth.sign_in_with_custom_token(token)
    uid = user['idToken']   
    
    db = firebase.database()

    db.child("users").child(childName).set(data, uid)

    

def getConfig():
    config = {}
    f = open("../../Camera/config.txt", "r")
    for line in f:
        pair = line.split(':', 1)
        config[pair[0]] = pair[1].split('\n')[0]
    f.close()
    return config

def stream_handler(message):
    global db
    global cameraID
    global userID
    try:
        if message['event'] == 'put':
            print(message['data'])
            path = message['path'].split(',')[1].split('/')[0]
            path2 = message['path'].split(',')[0].split('/')[1]
            variable = message['path'].split('/')[2]
            cmessage = message['data']
            print(cameraID == path)
            print(userID == path2)
            print(variable == "posture")
            print(cmessage == True)

            if path == cameraID and path2 == str(userID):
                if variable == "seat_exceeded" and cmessage == True:
                    telebot.sendMessage(path2, "You sit too long")
                    data = {"seat_exceeded": False}
                    db.child("users").child(path2+','+path).update(data)
                elif variable == "posture" and cmessage == True:
                    print("Hello")
                    telebot.sendMessage(path2, "Your posture bro")
                    data = {"posture": False}
                    db.child("users").child(path2+','+path).update(data)

    except Exception as e:
        print(e)

def start_stream(user, camera, telegram_bot):
    global telebot
    global cameraID
    global userID
    global my_stream

    telebot = telegram_bot

    userID = user
    cameraID = camera

    _thread.start_new_thread(run_stream, (db,))

def run_stream(db):
    global my_stream
    my_stream = db.child("users").stream(stream_handler)

def close_stream():
    global my_stream
    my_stream.close()







    
