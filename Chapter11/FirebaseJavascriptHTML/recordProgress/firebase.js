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
	var moduleVar = document.getElementById('module').value;
	var stepVar = document.getElementById('step').value;
  //alert("Working");
	//here is the connection string see https://player.vimeo.com/video/331000887
	//var myDBConn = firebase.database();
	var database = firebase.database().ref();
	var myDataLoc = database.child('students/2122');
	var data = myDataLoc.push();
	data.set(
	    {
		name : nameVar,
		email : emailVar,
		module : moduleVar,
		step : stepVar
		
		}
		);
}