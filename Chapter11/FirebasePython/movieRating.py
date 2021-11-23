from firebase import firebase


myDB = firebase.FirebaseApplication('https://movies-database-95d35-default-rtdb.europe-west1.firebasedatabase.app/', None)
allRecords= myDB.get('/movies/', None)
for key in allRecords:
    ratingVal= allRecords[key]['Rating'], end="\n"
    

counter = 0
for counter in range(3):
    movieName = input("enter movie name: ")
    rating = int(input("enter rating 1-5: "))
    movie = {"Movie Name" : movieName,
            "Rating" : rating}
    myDBConn.post ('/movies/', movie)
    counter +=1


    
    


