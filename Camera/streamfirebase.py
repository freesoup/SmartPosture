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
	while True:
		try:
			print ('test')
			time.sleep(5)
		except Exception as e:
			time.sleep(2)
			print ('test')

try:
   _thread.start_new_thread( run_stream, () )
   _thread.start_new_thread( take_picture, () )
except:
   print ("Error: unable to start thread")
   
while 1:
   pass
   
   