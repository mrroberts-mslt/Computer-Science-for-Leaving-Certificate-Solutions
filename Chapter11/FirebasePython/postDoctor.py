from firebase import firebase

myDB = firebase.FirebaseApplication("https://drpatients-68bc6-default-rtdb.firebaseio.com/", None )

record = {
    "docFN" :   "David",
    "docLN" :   "Doolittle"
}

myDB.post("/doctors/",record)
