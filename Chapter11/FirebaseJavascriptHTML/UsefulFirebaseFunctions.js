//------------------Insert Data Function  -------------------//
function insertData(){
//set makes the rollbox value the unique id if the same rollbox value is entered its overwritten
  set(ref(db, "TheStudents/"+ rollbox.value),{
  //push will add a unique value to the DB
  //push(ref(db, "TheStudents/"),{
    NameofStu: namebox.value,
    RollNumber: rollbox.value,
    Section: secbox.value,
    Gender: genderbox.value
  })
  .then(()=>
          {alert("Data stored successfully");
})
.catch((error)=>
          {alert("Error"+error);

});
}

//------------------UPDATE FUNCTION--------------------------//
function updateData(){
  update(ref(db, "TheStudents/"+ rollbox.value),{

    NameofStu: namebox.value,
    RollNumber: rollbox.value,
    Section: secbox.value,
    Gender: genderbox.value
  })
  .then(()=>
          {alert("Data updated successfully");
})
.catch((error)=>
          {alert("Error"+error);

});
}
//------------------SELECT  FUNCTION--------------------------//
function selectData(){
//A data snaphot contains data from a specific location
const dbref = ref(db);
get(child(dbref,"TheStudents/"+rollbox.value)).then((snapshot)=>{
  if (snapshot.exists()){
  namebox.value = snapshot.val().NameofStu;
  secbox.value = snapshot.val().Section;
  genderbox.value = snapshot.val().Gender;

  }
  else {
    alert("No data found");
  }
})
  .catch((error)=>
            {alert("Error"+error);
});

}
//------------------DELETE FUNCTION--------------------------//
function removeData(){
  remove(ref(db, "TheStudents/"+ rollbox.value),{
    NameofStu: namebox.value,
    RollNumber: rollbox.value,
    Section: secbox.value,
    Gender: genderbox.value
  })
  .then(()=>
          {alert("Data removed successfully");
})
.catch((error)=>
          {alert("Error"+error);

});
}


//------------------FILLING THE TABLE FUNCTION--------------------------//
var stdNo = 0;
var tbody = document.getElementById('tbody1');
function AddItemToTable(name,roll,sec,gen){
  let trow = document.createElement('tr');
  let td1 = document.createElement('td');
  let td2 = document.createElement('td');
  let td3 = document.createElement('td');
  let td4 = document.createElement('td');
  let td5 = document.createElement('td');

  td1.innerHTML=++stdNo;
  td2.innerHTML=name;
  td3.innerHTML=roll;
  td4.innerHTML=sec;
  td5.innerHTML=gen;

  trow.appendChild(td1);
  trow.appendChild(td2);
  trow.appendChild(td3);
  trow.appendChild(td4);
  trow.appendChild(td5);
  tbody.appendChild(trow);
}
function AddAllItemsToTable(TheStudents){
  stdNo=0;
  tbody.innerHTML="";
  TheStudents.forEach(element => {
    AddItemToTable(element.NameofStu, element.RollNumber, element.Section, element.Gender);
  });
}
//------------------GET ALL DATA ONCE NEED TO REFRESH TO LOAD DATA-------------------------//
function GetAllDataOnce(){
  const dbref = ref(db);
  get(child(dbref, "TheStudents"))
  .then((snapshot)=>{
    var students=[];
    snapshot.forEach(childSnapshot =>{
      students.push(childSnapshot.val());

    });
    AddAllItemsToTable(students);
  });
}
//------------------GET REALTIME DATA -------------------------//


 function GetDataRealTime(){
   const dbref = ref(db,"TheStudents");
   onValue(dbref,(snapshot)=>{
     var students=[];
     snapshot.forEach(childSnapshot => {
       students.push(childSnapshot.val());
     });
     AddAllItemsToTable(students);
   });
 }

//------ THIS WILL LOAD WHATEVER FUNCTION ON PAGE LOAD ------------//
window.onload = (GetDataRealTime());

