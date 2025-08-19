import pyrebase

config = {
  "apiKey": "AIzaSyBZ6JF9_u7vcwKml1KfDccxoIKOfREzJLY",
  "authDomain": "test-a9874.firebaseapp.com",
  "projectId": "test-a9874",
  "storageBucket": "test-a9874.appspot.com",   # ✅ corrected
  "messagingSenderId": "967639972068",
  "appId": "1:967639972068:web:b6c5510a27d14f59c814f1",
  "measurementId": "G-MWETV3QXG7",             # ✅ fixed key name
  "databaseURL": "https://test-a9874-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(config)

# Get database reference
db = firebase.database()

# Example data to push
data = {
    "date": "19/8/2025",
    "message": "https://drive.google.com/file/d/1nSwlTRGPyJpPhi2b6RBbjWWlREHy1JF4/view?usp=drive_link"
}

db.child("dATA").push(data)

print("✅ Data sent successfully")
