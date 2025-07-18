const colors = ["green", "red", "rgba(133,122,200)", "#f15025"];
const btn = document.getElementById('button'); //ngehubungin button ke js jadiin const
const color = document.querySelector(".color"); // dama ajh tapi karena class pake queryselector

button.addEventListener("click", changebg);//perintah pertama "eventnya" ngapain, kedua kemana
function changebg() {
    // console.log("bisa")
    const randomNumber = getRandomNumber();
    console.log(randomNumber)

    document.body.style.backgroundColor = colors[randomNumber];
    color.textContent = colors[randomNumber];
}

function getRandomNumber() {
    return Math.floor(Math.random() * colors.length);
    //math random cari random number di kali length jadi kalo 0.4 * 1 = 1.4 trus
    //dibuletin pake math floor 1.4 = 1 karena var 1 ada di const array maka nyambung
}