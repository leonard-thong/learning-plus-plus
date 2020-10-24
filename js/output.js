const fs = require("fs");

function outputFn() {
    document.getElementById("logoPng").style.visibility = "hidden";
    document.getElementById("questionText").style.visibility = "hidden";
    document.getElementById("pasteLinkBT").style.visibility = "hidden";
    document.getElementById("pasteLinkTB").style.visibility = "hidden";
    document.getElementById("computerDiv").style.visibility = "hidden";
    document.getElementById("ytDiv").style.visibility = "hidden";
    var rawContent = fs.readFileSync("input.json");
    var content = JSON.parse(rawContent);
    content.forEach(function (element) {
        var value = Object.values(element)[0];
        var key = Object.keys(element)[0];
        var array = value.split("|");
        console.log(array);
        ipcRenderer.send("item:key", key);
        array.forEach(function (arr) {
            ipcRenderer.send("item:add", arr);
        });
    });
}
