from firebase import Firebase


myDBConn = firebase.FirebaseApplication('https://drpatients-68bc6-default-rtdb.firebaseio.com/', None)
record1 = {
"firstName" : "Huw",
"lastName" : "Roberts",
"phoneNum" : "09090909",
"age" : "44",
"dob" : "01/01/70"

    }
#db name here
myDBConn.post ('/patients/', record1)
