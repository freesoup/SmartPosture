import pyrebase
import _thread
import time

db = None

def initCamera(userID, cameraID):
	user = userID + "," + cameraID

def stream_handler(message):
	global db
	try:
		if message['event'] == 'put':
			path = message['path'].split(',')[1].split('/')[0]
			#hard coded camera ID
			if path == '12' and message['data'] == 'True':
				take_picture(False)
				data = {"calibrate": "False"}
				db.child("users").child(message['path'].split(',')[0].split('/')[1] + ',' + path).set(data)
	except Exception as e:
		pass

def run_stream(db):
	my_stream = db.child("users").stream(stream_handler)

def check_posture():
	while True:
		take_picture(True)
		time.sleep(5)
		
def take_picture(check):
	#TODO: Add RPI camera code
	if check:
		print ("test")
		#TODO: CV stuff
	else:
		users_list = db.child("users").get()
		for user in users_list.each():
			#hard coded camera ID
			if user.key().split(',')[1] == 12:
				storage.child("users").child(user.key() + "/Image.jpg").put("asd.jpeg", uid)
				url = storage.child("users").child(user.key() + "/Image.jpg").get_url(uid)
				data = {"UserID" : user.key(), "Image" : url}
				db.child("users").child(user.key() + "/Images.jpg").set(data)
	
def main():
	config = {}
	f = open("config.txt", "r")
	for line in f:
		pair = line.split(':', 1)
		config[pair[0]] = pair[1].split('\n')[0]
	f.close()

	firebase = pyrebase.initialize_app(config)
	global db
	db = firebase.database()
	storage = firebase.storage()
	additional_claims = {
	  'premiumAccount': True
	}
	auth = firebase.auth()
	token = auth.create_custom_token("test", additional_claims)
	user = auth.sign_in_with_custom_token(token)
	uid = user['idToken']

	try:
	   _thread.start_new_thread(run_stream, (db,))
	   #_thread.start_new_thread(check_posture, ())
	except:
	   print ("Error: unable to start thread")
	   
	while 1:
	   pass

if __name__ == "__main__":
	main()
	
	