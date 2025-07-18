function increment() {
    var score = parseInt(document.querySelector(".score").innerHTML)
    document.querySelector(".score").innerHTML = score + 1
    // parse int = tolong ubah menajadi string yaitu class score dimana yang diubah itu content html
}

function decrement() {
    var score = parseInt(document.querySelector(".score").innerHTML)

    if (score > 0) {
        document.querySelector(".score").innerHTML = score - 1
    }

}