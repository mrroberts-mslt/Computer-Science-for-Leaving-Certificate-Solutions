from firebase import firebase

myDB = firebase.FirebaseApplication("https://doctorpatients-4a24a-default-rtdb.firebaseio.com/", None)

docRecords = myDB.get("/doctors/", None)

for key in docRecords:
    print(key)

# for i in docRecords:
#     print(docRecords[i]["docFN"], end="\t")
#     print(docRecords[i]["docLN"], end="\t")
#     print()
