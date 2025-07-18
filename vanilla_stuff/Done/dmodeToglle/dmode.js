const toggle = document.getElementById("toggle");
console.log(toggle)
toggle.addEventListener("change", (e) => {
    document.body.classList.toggle("dark", e.target.checked);
})