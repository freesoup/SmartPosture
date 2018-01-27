import pyrebase

def requestTakePic(childName):
    config = getConfig()

    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    #retrieve userid from auth token

    additional_claims = {
	  'premiumAccount': True
	}

    auth = firebase.auth()
    token = auth.create_custom_token("test", additional_claims)
    user = auth.sign_in_with_custom_token(token)
    uid = user['idToken']   
    
    db = firebase.database()

    db.child(users).child(childName).update({"calibrate":True}, uid)

    
    
    
