window.fbAsyncInit = function() {
    FB.init({
        appId      : '888453084543808',
        xfbml      : true,
        version    : 'v2.4'
    });
    FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
            console.log('Logged in.');
        }
        else {
            FB.login();
        }
    });
};

(function(d, s, id){
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {return;}
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

function myFacebookLogin() {
    FB.login(
        function(){
            FB.api(
                "/me/photos",
                "POST",
                {
                    message: "My Emoji!!",
                    url: "http://line25.com/wp-content/uploads/2010/facebook/1.png"
                },
                function (response) {
                    if (!response && response.error) {
                        alert("Post Failed!");
                    }
                    else{
                        alert("Post Success!");
                    }
                }
            );
        },
        {scope: 'publish_actions'}
    );
}

function confirmPage() {
    if (confirm("Sure to post your Emoji") == true) {
        alert("Running");
        myFacebookLogin();
    }   
    else {
        alert("Error");//confirmPage();
    }
}