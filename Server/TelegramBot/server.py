import pyrebase

def requestTakePic(childName):
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

    
