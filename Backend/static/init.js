/**
 * Created by renl on 9/11/15.
 */

window.addEventListener("DOMContentLoaded", function() {
    var faceAPIs = initFaceAPIs();
	var liveFace = document.getElementById("liveFace"),
		liveFaceObj = { "video": true},
        canvas = document.getElementById("snapCanvas"),
        context = canvas.getContext("2d");
        document.getElementById("snapButton").addEventListener("click", function() {
            context.drawImage(liveFace, 0, 0, 320, 240);
            canvas.style.display = "block";
            var binaryString = atob(canvas.toDataURL().replace(/^data:image\/(png|jpg);base64,/, ""));
            faceAPIs.microsoftAPI(binaryString).done(function(data) {
            	console.log(data)
            });
        });
        document.getElementById("clearButton").addEventListener("click", function() {
            canvas.style.display = "none";
        });
		errBack = function(error) {
			console.log("Video capture error: ", error.code);
		};
	if(navigator.getUserMedia) { // Standard
		navigator.getUserMedia(liveFaceObj, function(stream) {
			liveFace.src = stream;
			liveFace.play();
		}, errBack);
	} else if(navigator.webkitGetUserMedia) { // WebKit-prefixed
		navigator.webkitGetUserMedia(liveFaceObj, function(stream){
			liveFace.src = window.URL.createObjectURL(stream);
			liveFace.play();
		}, errBack);
	}
	else if(navigator.mozGetUserMedia) { // Firefox-prefixed
		navigator.mozGetUserMedia(liveFaceObj, function(stream){
			liveFace.src = window.URL.createObjectURL(stream);
			liveFace.play();
		}, errBack);
	}
}, false);

function initFaceAPIs() {
    var faceAPIs = FaceAPIs();
    return faceAPIs;
}