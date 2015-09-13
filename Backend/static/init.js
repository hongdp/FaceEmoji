/**
 * Created by renl on 9/11/15.
 */

window.addEventListener("DOMContentLoaded", function () {
    var liveFace = document.getElementById("liveFace"),
        liveFaceObj = {"video": true},
        canvas = document.getElementById("snapCanvas"),
        context = canvas.getContext("2d");
    document.getElementById("snapButton").addEventListener("click", function () {
        context.drawImage(liveFace, 0, 0, 320, 240);
        var emojiCanvas = document.getElementById("emojiCanvas");
        if (emojiCanvas) {
            emojiCanvas.parentNode.removeChild(emojiCanvas);
        }
        var emojiCanvas = document.createElement("canvas");
        emojiCanvas.id = "emojiCanvas";
        emojiCanvas.width = "320";
        emojiCanvas.height = "240";
        var ctx = emojiCanvas.getContext("2d");
        ctx.font = "48px serif";
        ctx.fillText('Loading...', 60, 150);
        document.getElementById("emojiDashborad").insertBefore(emojiCanvas, postButton);
        canvas.style.display = "inline";
        var dataURL = canvas.toDataURL();
        var dataString = dataURL.split(',')[1];
        var http = new XMLHttpRequest();
        var serviceEndpoint = "/blob";
        http.open("post", serviceEndpoint, true);
        http.onreadystatechange = function() {
            if (http.readyState==4 && http.status==200) {
                faces = JSON.parse(http.response);
                drawEmojisByFaces(faces);
            }
        };
        http.send(dataString);
    });
    document.getElementById("clearButton").addEventListener("click", function () {
        canvas.style.display = "none";
        var emojiCanvas = document.getElementById("emojiCanvas");
        console.log(emojiCanvas);
        emojiCanvas.parentNode.removeChild(emojiCanvas);
        document.getElementById("postButton").style.display = "none";
    });
    errBack = function (error) {
        console.log("Video capture error: ", error.code);
    };
    if (navigator.getUserMedia) { // Standard
        navigator.getUserMedia(liveFaceObj, function (stream) {
            liveFace.src = stream;
            liveFace.play();
        }, errBack);
    } else if (navigator.webkitGetUserMedia) { // WebKit-prefixed
        navigator.webkitGetUserMedia(liveFaceObj, function (stream) {
            liveFace.src = window.URL.createObjectURL(stream);
            liveFace.play();
        }, errBack);
    }
    else if (navigator.mozGetUserMedia) { // Firefox-prefixed
        navigator.mozGetUserMedia(liveFaceObj, function (stream) {
            liveFace.src = window.URL.createObjectURL(stream);
            liveFace.play();
        }, errBack);
    }
}, false);

function drawEmojisByFaces(data) {
    console.log(data);
    var emojiCanvas = document.getElementById("emojiCanvas");
    if (emojiCanvas) {
        emojiCanvas.parentNode.removeChild(emojiCanvas);
    }
    var emojiCanvas = document.createElement("canvas");
    emojiCanvas.id = "emojiCanvas";
    emojiCanvas.width = "320";
    emojiCanvas.height = "240";
    var ctx = emojiCanvas.getContext("2d");
    img = document.getElementById("smile");
    var emoji_list = data.emoji_list;
    var face_data = data.face_data;
    for (var i = 0; i < face_data.length; i++) {
        var face = face_data[i];
        var emoji_name = emoji_list[i];
        var angle = face.angle,
            top = face.top,
            left = face.left,
            width = face.width,
            height = face.height;
        ctx.rotate(angle * Math.PI / 180);
        var img = document.getElementById('../static/'+emoji_name+'.png');
        console.log(img);
        ctx.drawImage(img, left, top, width, height);
    }
    emojiCanvas.style.display = "inline";
    document.getElementById("emojiDashborad").insertBefore(emojiCanvas, postButton);
    postPrepare(function() {
        var confirmButton = document.getElementById("confirmButton");
        var postButton = document.getElementById("postButton");
        postButton.style.display = "block";
    });
}