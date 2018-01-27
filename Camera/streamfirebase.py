import pyrebase
import _thread
import time

config = {}

f = open("config.txt", "r")
for line in f:
	pair = line.split(':', 1)
	config[pair[0]] = pair[1].split('\n')[0]
f.close()

firebase = pyrebase.initialize_app(config)

db = firebase.database()
storage = firebase.storage()

additional_claims = {
  'premiumAccount': True
}

token = auth.create_custom_token("test", additional_claims)
user = auth.sign_in_with_custom_token(token)
uid = user['idToken']

userfile = "331,33"

#data = {"action":"Nothing"}
#db.child("users").child("123,12").set(data)


def initCamera(userID, cameraID):
	user = userID + "," + cameraID


def stream_handler(message):
	try:
		if message['event'] == 'put':
			path = message['path'].split(',')[1].split('/')[0]
			if path == '12':
				print (message['data'])
	except Exception as e:
		pass

def run_stream():
	my_stream = db.child("users").stream(stream_handler)

def take_picture():
    storage.child("users").child(userfile + "/Image.jpg").put("asd.jpeg", uid)
    url = storage.child("users").child(userfile + "/Image.jpg").get_url(uid)

    data = {"UserID" : userfile, "Image" : url}
    db.child("users").child(userfile + "/Images.jpg").set(data)

try:
   _thread.start_new_thread( run_stream, () )
   _thread.start_new_thread( take_picture, () )
except:
   print ("Error: unable to start thread")
   
while 1:
   pass
   
   