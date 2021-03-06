window.fbAsyncInit = function () {
    FB.init({
        appId: '905262636233094',
        xfbml: true,
        version: 'v2.4'
    });
    FB.getLoginStatus(function (response) {
        if (response.status === 'connected') {
        }
        else {
            FB.login();
        }
    });
};

(function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {
        return;
    }
    js = d.createElement(s);
    js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

function myFacebookLogin() {
    FB.login(
        function () {
            FB.api(
                "/me/photos",
                "POST",
                {
                    message: "Our Selfie Emoji!",
                    url: combineimage_url
                },
                function (response) {
                    if (!response && response.error) {
                        alert("Post Failed!");
                    }
                }
            );
        },
        {scope: 'publish_actions'}
    );
}

function confirmPage() {
    if (confirm("Sure to post your Emoji") == true) {
        myFacebookLogin();
    }
    else {
        alert("Error");//confirmPage();
    }
}

function voiceControl() {
    window.SpeechRecognition = window.SpeechRecognition ||
    window.webkitSpeechRecognition ||
    null;
    if (window.SpeechRecognition === null) {
        document.getElementById('ws-unsupported').classList.remove('hidden');
        document.getElementById('button-play-ws').setAttribute('disabled', 'disabled');
        document.getElementById('button-stop-ws').setAttribute('disabled', 'disabled');
    }
    else {
        console.log("speech recognition");
        var recognizer = new window.SpeechRecognition();
        recognizer.continuous = false;
        recognizer.onresult = function (event) {
            for (var i = event.resultIndex; i < event.results.length; i++) {
                if (event.results[i].isFinal) {
                    if (event.results[i][0].transcript == 'post'
                        || event.results[i][1].transcript == 'post'
                        || event.results[i][2].transcript == 'post'
                        || event.results[i][3].transcript == 'post'
                        || event.results[i][4].transcript == 'post'
                    ) {
                        myFacebookLogin();
                        $("#myModal").modal('hide');
                    }
                }
            }
        };
        recognizer.start();
    }
}

