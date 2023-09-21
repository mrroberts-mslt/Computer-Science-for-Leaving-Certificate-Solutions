// Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.4.0/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.4.0/firebase-analytics.js";

  const firebaseConfig = {
    apiKey: "AIzaSyCKSaHHTZatSzn1e83eUlyWrFqJm319o8s",
    authDomain: "formtofirebase.firebaseapp.com",
    databaseURL: "https://formtofirebase-default-rtdb.europe-west1.firebasedatabase.app",
    projectId: "formtofirebase",
    storageBucket: "formtofirebase.appspot.com",
    messagingSenderId: "468623891511",
    appId: "1:468623891511:web:f2e37a85e6081e6b2533b2",
    measurementId: "G-RTF3Q5D2WS"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);

  //Add these lines to include the modules required for managing the database.
  import {getDatabase,set,ref,get,child,update,remove,push,increment}
  from "https://www.gstatic.com/firebasejs/10.4.0/firebase-database.js";

  const db = getDatabase();
//End of Firebase Stuff

// Insert data into Database  
 function insertData(){
            let name = document.getElementById('name').value;
            let age = document.getElementById('age').value;
            let occupation = document.getElementById('occupation').value;

            // Push user data to the Firebase Realtime Database
            push(ref(db,'users'),{
                name: name,
                age: age,
                occupation: occupation
    })
    .then(()=>
            {alert("Data stored successfully");
  })
  .catch((error)=>
            {alert("Error"+error);

  });
  }
insertBtn.addEventListener("click", insertData);
