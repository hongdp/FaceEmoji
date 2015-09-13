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
        canvas.style.display = "inline";
        var dataURL = canvas.toDataURL();
<<<<<<< HEAD
        var blobBin = atob(dataURL.split(',')[1]);
        var array = [];
        for (var i = 0; i < blobBin.length; i++) {
            array.push(blobBin.charCodeAt(i));
        }
        var blob = new Blob([new Uint8Array(array)], {type: 'image/png'});
        faceAPIs.microsoftAPI(blob, function(data) {
            console.log(data);
            // $.ajax({
            // 	type: "POST",
            // 	url: "/REST",
            // 	contentType: "application/json",
            // 	data: {
            // 		'title': "hello",
            // 		'description': "world"
	           //  },
	           //  dataType: "json",
	           //  success: function(data) {
	           //  	console.log(data);
	           //  }
            // })
        	var temp = {title: "hello", description: "world"};
        	var http = new XMLHttpRequest();
	        var apiUrl = "/REST";
	        http.open("post", apiUrl, true);
	        // http.setRequestHeader("Content-Type","application/json");
	        http.onreadystatechange = function() {
	        	if (http.readyState == 4 && http.status == 200) {
					console.log(http.response);
				}
	        };
	        http.send(temp);
        });
=======
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
>>>>>>> 813bb4a384d15b0d7be7bae76aa626f7addc7a94
    });
    document.getElementById("clearButton").addEventListener("click", function () {
        canvas.style.display = "none";
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
    console.log(faces);
    var emojiCanvas = document.getElementById("emojiCanvas");
    console.log(emojiCanvas);
    var ctx = emojiCanvas.getContext("2d");
    img = document.getElementById("smile");
    for (var i = 0; i < faces.length; i++) {
        var face = faces[i];
        var angle = face.attributes.headPose.roll;
        var top = face.faceRectangle.top;
        var left = face.faceRectangle.left;
        var width = face.faceRectangle.width;
        var height = face.faceRectangle.height;
        ctx.rotate(angle * Math.PI / 180);
        ctx.drawImage(img, left, top, width, height);
    }
    emojiCanvas.style.display = "inline";
    document.getElementById("postButton").style.display = "block";
}