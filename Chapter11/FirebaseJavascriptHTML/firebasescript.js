alert("working!");
// Your web app's Firebase configuration
var config = {
    apiKey: "AIzaSyDDyEEp7dpnBQvged-vldCaraXiqAzSFns",
    authDomain: "typythonprogress.firebaseapp.com",
    databaseURL: "https://typythonprogress-default-rtdb.europe-west1.firebasedatabase.app",
    projectId: "typythonprogress",
    storageBucket: "typythonprogress.appspot.com",
    messagingSenderId: "657906864581",
    appId: "1:657906864581:web:087b3cf319de1b5342bbac"
  };
  

  firebase.initializeApp(config);

  // Get a reference to the database service
  
  
  
// Initialize Firebase
//firebase.initializeApp(firebaseConfig);
  


function insertRecord() {
	var nameVar = document.getElementById('name').value;
	var emailVar = document.getElementById('email').value;
	var mobileVar = document.getElementById('mobile').value;
  var database = firebase.database().ref();
	var myDataLoc = database.child('students/2122');
	var data = myDataLoc.push();
	data.set(
	    {
		name : nameVar,
		email : emailVar,
		mobile : mobileVar
		
		}
		);
}
