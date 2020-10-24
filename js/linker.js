const { PythonShell } = require("python-shell");
const { dialog } = require("electron").remote;
var path = require("path");

function pasteLink() {
    document.getElementById("pasteLinkTB").style.visibility = "visible";
    document.getElementById("pasteLinkBT").style.visibility = "visible";
}

function uploadFile() {
    var pathTwo = dialog.showOpenDialogSync()[0];

    var options = {
        scriptPath: path.join(__dirname, "/engine/"),
        args: [pathTwo],
    };

    let pyshell = new PythonShell("main.py", options);

    pyshell.on("message", function (message) {
        alert(message);
    });
}

function uploadFileTwo() {
    var link = document.getElementById("pasteLinkTB").value;

    var options = {
        scriptPath: path.join(__dirname, "/engine/"),
        args: [link],
    };

    let pyshell = new PythonShell("main.py", options);

    pyshell.on("message", function (message) {
        alert(message);
    });
}
