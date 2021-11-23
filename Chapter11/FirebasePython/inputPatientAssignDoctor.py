from firebase import firebase

myDB = firebase.FirebaseApplication("https://drpatients-68bc6-default-rtdb.firebaseio.com/", None)

docRecords = myDB.get("doctors", None)

docPKeys = []
docNames = []


for key in docRecords:
    docPKeys.append(key)
    docName = docRecords[key]["docFN"] + " " + docRecords[key]["docLN"]
    docNames.append(docName)
    
print()
pFName = input("Patients First Name   : ")
pLName = input("Patients Last Name    : ")
pPNum  = input("Patients Phone Number : ")
pAge   = input("Patients age          : ")

#make a numerical list of all the doctors in the table
counter = 1
for doc in docNames:
    print(counter, ")\t", doc)
    counter += 1
    
docIndex = int(input("Please select patient doctor:")) - 1
#assign the index value of the list as the foreign key
if docIndex+1 > len(docPKeys):
    print("Error")
    docIndex = int(input("Please select patient doctor:")) - 1
    
else:
    forKey = docPKeys[docIndex]

    record = {
        "firstName"  :   pFName,
        "lastName"   :   pLName,
        "phoneNum"   :   pPNum,
        "age"        :   pAge,
        "forKey"     :   forKey
        }

    myDB.post('/patients/', record)
