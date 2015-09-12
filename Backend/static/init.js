/**
 * Created by renl on 9/11/15.
 */

window.addEventListener("DOMContentLoaded", function () {
    var faceAPIs = initFaceAPIs();
    var liveFace = document.getElementById("liveFace"),
        liveFaceObj = {"video": true},
        canvas = document.getElementById("snapCanvas"),
        context = canvas.getContext("2d");
    document.getElementById("snapButton").addEventListener("click", function () {
        context.drawImage(liveFace, 0, 0, 320, 240);
        canvas.style.display = "block";
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
        if (emojiCanvas) {
            emojiCanvas.parentNode.removeChild(emojiCanvas);
        }
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

function initFaceAPIs() {
    var faceAPIs = FaceAPIs();
    return faceAPIs;
}

function drawEmojisByFaces(faces) {
    var emojiCanvas = document.createElement('canvas');
    emojiCanvas.id = "emojiCanvas";
    var ctx = emojiCanvas.getContext("2d");
    emojiCanvas.width = "320";
    emojiCanvas.height = "240";
    img = document.getElementById("smile");
    console.log(img);
    for (var i = 0; i < faces.length; i++) {
        var face = faces[i];
        var angle = face.attributes.headPose.roll;
        var top = face.faceRectangle.top;
        var left = face.faceRectangle.left;
        var width = face.faceRectangle.width;
        var height = face.faceRectangle.height;
        console.log("top");
        console.log(top);
        console.log("left");
        console.log(left);
        console.log("width");
        console.log(width);
        console.log("height");
        console.log(height);

        console.log(angle);
        ctx.rotate(angle * Math.PI / 180);
        ctx.drawImage(img, left, top, width, height);
    }


    var emojiCanvasContainer = document.getElementById("emojiCanvasContainer");
    emojiCanvasContainer.appendChild(emojiCanvas);
}