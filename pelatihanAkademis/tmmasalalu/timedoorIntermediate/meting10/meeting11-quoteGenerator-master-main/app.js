var quotes = ["quotes 1", "quotes 2", "quotes 3"];

function generate() {
    //generate random
    let random = Math.floor(Math.random() * quotes.length);
    document.getElementById('quoteSection').
        innerHTML = quotes[random];
}

function seeAllQuotes() {
    text = "<ul>";
    for (i = 0; i < quotes.length; i++) {
        text += "<li>" + quotes[i] + "</li>";
    }

    text += "</ul>";
    document.getElementById("quoteSection").innerHTML = text;
}

function newQuotes() {
    var newQuotes = document.getElementById("insertSection").value;
    alert("quotes added");
    quotes.push(newQuotes);
    seeAllQuotes();
}