const hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"];
const button = document.querySelector("#button")
const color = document.querySelector(".color")

button.addEventListener("click", changeBgHex)

function changeBgHex() {
    let hexColor = "#" //hex color harus ada #
    for (let i = 0; i < 6; i++) {
        hexColor += hex[getRandomNumber()]
    }
    color.textContent = hexColor;
    document.body.style.backgroundColor = hexColor;
    console.log(getRandomNumber())
}

function getRandomNumber() {
    return Math.floor(Math.random() * hex.length);
    //The return statement stops the execution of a function and returns a value
}
