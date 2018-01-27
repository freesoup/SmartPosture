import pyrebase
import _thread
import time

db = None
cameraID = '12'

def stream_handler(message):
	global db
	global cameraID
	try:
		if message['event'] == 'put':
			path = message['path'].split(',')[1].split('/')[0]
			#hard coded camera ID
			if path == cameraID and message['data'] == 'True':
				take_picture(False)
				data = {"calibrate": "False"}
				db.child("users").child(message['path'].split(',')[0].split('/')[1] + ',' + path).set(data)
	except Exception as e:
		pass

def run_stream(db):
	my_stream = db.child("users").stream(stream_handler)

def check_posture(db, cameraID):
	time_count = 0
	while True:
		sit_check = take_picture(True)
		time.sleep(5)
		if sit_check == True:
			time_count += 5
			if time_count > 1200:
				users_list = db.child("users").get()
				for user in users_list.each():
					#hard coded camera ID
					if user.key().split(',')[1] == cameraID:
						data = {"timer": time_count, "seat_exceeded": "True"}
						db.child("users").child(user.key()).set(data)
		else:
			time_count = 0
		
def take_picture(check):
	global db
	global cameraID
	#TODO: Add RPI camera code
	if check:
		print ("test")
		#TODO: CV stuff
	else:
		users_list = db.child("users").get()
		for user in users_list.each():
			#hard coded camera ID
			if user.key().split(',')[1] == cameraID:
				storage.child("users").child(user.key() + "/Image.jpg").put("asd.jpeg", uid)
				url = storage.child("users").child(user.key() + "/Image.jpg").get_url(uid)
				data = {"UserID" : user.key(), "Image" : url}
				db.child("users").child(user.key() + "/Images.jpg").set(data)
	
def main():
	global db
	global cameraID
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
	auth = firebase.auth()
	token = auth.create_custom_token("test", additional_claims)
	user = auth.sign_in_with_custom_token(token)
	uid = user['idToken']

	try:
	   _thread.start_new_thread(run_stream, (db,))
	   #_thread.start_new_thread(check_posture, (db,cameraID, ))
	except:
	   print ("Error: unable to start thread")
	   
	while 1:
	   pass

if __name__ == "__main__":
	main()
	
	