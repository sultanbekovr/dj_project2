function loadAgeSelector() {
    let startyear = 1900;
    let endyear = 2014;
    for (let i = startyear; i<=endyear; i++){
        node = document.createElement("Option");
        textnode = document.createTextNode(i);
        node.appendChild(textnode);
        document.getElementById("yearselect").appendChild(node);
    }
}