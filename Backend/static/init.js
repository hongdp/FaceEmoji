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
