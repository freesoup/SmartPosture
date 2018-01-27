import pyrebase
import _thread
import time

config = {
  "apiKey": "AIzaSyDBqip-V77GxAq_b2FWEJ51EBSfuWpSDo0",
  "authDomain": "hacknr-a5b65.firebaseapp.com",
  "databaseURL": "https://hacknr-a5b65.firebaseio.com/",
  "storageBucket": "hacknr-a5b65.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

#data = {"action":"Nothing"}
#db.child("users").child("123,12").set(data)

def stream_handler(message):
	try:
		if message['event'] == 'put':
			path = message['path'].split(',')[1].split('/')[0]
			if path == '12':
				print (message['data'])
	except:
		pass

def run_stream():
	my_stream = db.child("users").stream(stream_handler)

def take_picture():
	while True:
		try:
			print ('test')
			time.sleep(5)
		except:
			time.sleep(2)
			print ('test')

try:
   _thread.start_new_thread( run_stream, () )
   _thread.start_new_thread( take_picture, () )
except:
   print ("Error: unable to start thread")
   
while 1:
   pass
	

	
	