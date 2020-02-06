const fs = require("fs");

// In the main process.

// Or use `remote` from the renderer process.
// const { BrowserWindow } = require('electron').remote

function outputFn() {
  // Or load a local HTML file
  // const { BrowserWindow } = require("electron");
  // const BrowserWindow = electron.remotel.BrowserWindow;
  // const child = new BrowserWindow({
  //   width: 800,
  //   height: 800
  // });
  // win.on("closed", () => {
  //   win = null;
  // });
  // win.loadURL(`file://${__dirname}/output.html`);
  // window.open("output.html");
  document.getElementById("logoPng").style.visibility = "hidden";
  document.getElementById("questionText").style.visibility = "hidden";
  document.getElementById("pasteLinkBT").style.visibility = "hidden";
  document.getElementById("pasteLinkTB").style.visibility = "hidden";
  document.getElementById("computerDiv").style.visibility = "hidden";
  document.getElementById("ytDiv").style.visibility = "hidden";
  var rawContent = fs.readFileSync("input.json");
  var content = JSON.parse(rawContent);
  // var stringContent = JSON.stringify(content);
  content.forEach(function(element) {
    // console.log(Object.keys(element)[0]);
    var value = Object.values(element)[0];
    var key = Object.keys(element)[0];
    var array = value.split("|");
    // console.log(Object.values(element)[0]);
    console.log(array);
    ipcRenderer.send("item:key", key);
    array.forEach(function(arr) {
      // console.log(arr);
      ipcRenderer.send("item:add", arr);
    });
  });
  // console.log(value);

  // ipcRenderer.send("item:add", value);
  // console.log(stringContent);
  // content.forEach(function(element) {
  //   console.log(Object.keys(element)[0]);
  //   var value = Object.values(element)[0];
  //   var array = value.split("|");
  //   // console.log(Object.values(element)[0]);
  //   // console.log(array);
  //   array.forEach(function(arr) {
  //     console.log(arr);
  //   });
  // });

  // var rawContent = fs.readFileSync(link.txt);
  // var content = rawContent.toString();

  // function getId(url) {
  //   var regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
  //   var match = url.match(regExp);

  //   if (match && match[2].length == 11) {
  //     return match[2];
  //   } else {
  //     return "error";
  //   }
  // }

  // var videoId = getId(content);

  // var iframeMarkup =
  //   '<iframe width="560" height="315" src="//www.youtube.com/embed/' +
  //   videoId +
  //   '" frameborder="0" allowfullscreen></iframe>';

  // var stupid = document.getElementById("ossas");
  // stupid.insertAdjacentHTML(null, iframeMarkup);
  // console.log(videoId);
}
