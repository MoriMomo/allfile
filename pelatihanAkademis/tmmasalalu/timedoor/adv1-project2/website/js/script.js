// // NAVBAR
// window.addEventListener("scroll", function () {
//     var nav = document.querySelector("nav");
//     nav.classList.toggle("sticky", window.scrollY > 0);
// })

//jumbotron
function changeText() {
    // alert("tes")
    var replaceText = document.getElementsByClassName("mini-text");
    replaceText[0].innerHTML = "scroll untuk melihat"

    document.getElementById("icon-up").style.display = "none";

    document.getElementById("icon-down").style.display = "block";

}

//button bellow pp
var btnLike = document.querySelector('#green')
var btnDislike = document.querySelector('#red')

btnLike.onclick = likeColor
btnDislike.onclick = dislikeColor

function likeColor() {
    if (btnDislike.classList.contains('red')) {
        btnDislike.classList.remove('red');
    }
    this.classList.toggle('green')
}

function dislikeColor() {
    if (btnDislike.classList.contains('green')) {
        btnDislike.classList.remove('green');
    }
    this.classList.toggle('red')
}

//image change js
function changeImage(element) {
    element.setAttribute("src", "/website/img/img-header2.png")
}

function changeImageBack(element) {
    element.setAttribute("src", "/website/img/img-header.png")
}

// silangnya
// var myList = document.getElementsByTagName("li")
// var i;
// for (i = 0; i < myList.length; i++) {
//     var span = document.createElement("span");
//     span.innerHTML = "x"
//     myList[i].appendChild(span).setAttribute("class", "close")
// }

// // eventnya
// var close = document.getElementsByClassName("close");
// var i;
// for (i = 0; i < close.length; i++) {
//     close[i].onClick = function () {
//         var div = this.parentElement;
//         div.style.display = "none"
//     }
// }

// function newElement() {
//     var li = document.createElement("li");
//     var inputValue = document.getElementById("myInput").value;

//     if (inputValue === '' || inputValue === '') {
//         alert("data tidak boleh kosong");
//     }
//     else {
//         document.getElementById("myUL").appendChild(li).setAttribute("class", "search-tags-item");
//         li.innerHTML = inputValue;
//     }

//     document.getElementById("myInput").value = "";

//     var span = document.createElement("SPAN");
//     span.innerHTML = "x";
//     li.appendChild(span).setAttribute("class", "close");

//     for (i = 0; i < close.length; i++) {
//         close[i].onClick = function () {
//             var div = this.parentElement;
//             div.style.display = "none"
//         }
//     }
// }

var myList = document.getElementsByTagName("li");
var i;
for (i = 0; i < myList.length; i++) {
    var span = document.createElement("span");
    span.innerHTML = "x";
    myList[i].appendChild(span).
        setAttribute("class", "close");
}


var close = document.
    getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
        var div = this.parentElement;
        div.style.display = "none"
    }
}


function newElement() {
    // Create new list with the inputed value
    // alert("BISA GAS")
    var li = document.createElement("li");
    var inputValue = document.
        getElementById("myInput").value;

    // Check the inputed value 
    if (inputValue === '' || inputValue === ' ') {
        alert("Data cannot be empty!");
    } else {
        document.getElementById("myUL").
            appendChild(li).setAttribute("class", "search-tags-item");
        li.innerHTML = inputValue;
    }

    // Clear text on the search bar
    document.getElementById("myInput").value
}
