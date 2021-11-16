from firebase import firebase

myDB = firebase.FirebaseApplication("https://doctorpatients-4a24a-default-rtdb.firebaseio.com/", None)

patientRecords = myDB.get("/patients/", None)

for i in patientRecords:
    print(patientRecords[i]["firstName"], end="\t")
    print(patientRecords[i]["lastName"], end="\t")
    print(patientRecords[i]["phoneNum"], end="\t")
    print(patientRecords[i]["age"], end="\t")
    print(patientRecords[i]["dob"], end="\t")
    print()
    
