function checkforphysics(){
    var value = document.getElementById("mathforphysics").checked;

    if (value === true){
        var myClasses = document.getElementsByClassName('notphysicsmath');
        for (var i = 0; i < myClasses.length; i++) {
            myClasses[i].style.display = 'none';
        }
    }
    else if (value === false){
        var myClasses = document.getElementsByClassName('notphysicsmath');
        for (var i = 0; i < myClasses.length; i++) {
            myClasses[i].style.display = '';
        }
    }
}