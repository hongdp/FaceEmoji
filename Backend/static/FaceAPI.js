function FaceAPIs() {
	// This function returns a JSON in following format:
	// [
	// 	{
	// 		"faceId": "c5c24a82-6845-4031-9d5d-978df9175426",
	// 		"faceRectangle": {
	// 			"top": 54,
	// 			"left": 394,
	// 			"width": 78,
	// 			"height": 78
	// 		},
	// 		"faceLandmarks": {
	// 			"pupilLeft": { "x": 412.7, "y": 78.4 },
	// 			"pupilRight": { "x": 446.8, "y": 74.2 },
	// 			"noseTip": { "x": 437.7, "y": 92.4 },
	// 			"mouthLeft": { "x": 417.8, "y": 114.4 },
	// 			"mouthRight": { "x": 451.3, "y": 109.3 },
	// 			"eyebrowLeftOuter": { "x": 397.9, "y": 78.5 },
	// 			"eyebrowLeftInner": { "x": 425.4, "y": 70.5 },
	// 			"eyeLeftOuter": { "x": 406.7, "y": 80.6 },
	// 			"eyeLeftTop": { "x": 412.2, "y": 76.2 },
	// 			"eyeLeftBottom": { "x": 413.0, "y": 80.1 },
	// 			"eyeLeftInner": { "x": 418.9, "y": 78.0 },
	// 			"eyebrowRightInner": { "x": 4.8, "y": 69.7 },
	// 			"eyebrowRightOuter": { "x": 5.5, "y": 68.5 },
	// 			"eyeRightInner": { "x": 441.5, "y": 75.0 },
	// 			"eyeRightTop": { "x": 446.4, "y": 71.7 },
	// 			"eyeRightBottom": { "x": 447.0, "y": 75.3 },
	// 			"eyeRightOuter": { "x": 451.7, "y": 73.4 },
	// 			"noseRootLeft": { "x": 428.0, "y": 77.1 },
	// 			"noseRootRight": { "x": 435.8, "y": 75.6 },
	// 			"noseLeftAlarTop": { "x": 428.3, "y": 89.7 },
	// 			"noseRightAlarTop": { "x": 442.2, "y": 87.0 },
	// 			"noseLeftAlarOutTip": { "x": 424.3, "y": 96.4 },
	// 			"noseRightAlarOutTip": { "x": 446.6, "y": 92.5 },
	// 			"upperLipTop": { "x": 437.6, "y": 105.9 },
	// 			"upperLipBottom": { "x": 437.6, "y": 108.2 },
	// 			"underLipTop": { "x": 436.8, "y": 111.4 },
	// 			"underLipBottom": { "x": 437.3, "y": 114.5 }
	// 		},

	// 		"attributes": {
	// 			"headPose": { "pitch": 0.0, "roll": -10.3, "yaw": 18.1 },
	// 			"gender": "male",
	// 			"age": 71.0
	// 		}
	// 	}
	// ]
	// Throw exception if error response is given.
	var CallMicrosoftAPI = function(blob, callBack) {
        var params = {
            // Request parameters
            "analyzesFaceLandmarks": "true",
            "analyzesAge": "true",
            "analyzesGender": "true",
            "analyzesHeadPose": "true"
        };
        var http = new XMLHttpRequest();
        var apiUrl = "https://api.projectoxford.ai/face/v0/detections?";
        http.open("post", apiUrl + $.param(params), true);
        http.setRequestHeader("Content-Type","application/octet-stream");
        http.setRequestHeader("Ocp-Apim-Subscription-Key","f4f23db3a4e244779bfa3f01bd6f89ca");
        http.onreadystatechange = function() {
        	if (http.readyState == 4 && http.status == 200) {
				callBack(JSON.parse(http.response));
			}
        };
        http.send(blob);
	};

	var CallFacePPAPI = function(photoBinary) {
		
	};

	return {
		microsoftAPI: CallMicrosoftAPI,
		facePPAPI: CallFacePPAPI
	};
}