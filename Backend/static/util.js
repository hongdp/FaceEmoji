function postPrepare(callback) {
    var can1 = document.getElementById('snapCanvas');
    var can2 = document.getElementById('emojiCanvas');
    console.log(can2);
    var canvas = document.getElementById('combineCanvas');
    var context = canvas.getContext('2d');

    canvas.width = 480;
    canvas.height = 180;
    context.drawImage(can1, 0, 0, 240, 180);
    context.drawImage(can2, 240, 0, 240, 180);
    var dataURL = canvas.toDataURL();
    var dataString = dataURL.split(',')[1];
    var http = new XMLHttpRequest();
    http.open("post", '/combine', true);
    http.onreadystatechange = function () {
        if (http.readyState == 4 && http.status == 200) {
            combineimage_url = http.response;
            var previewImage = document.getElementById("previewImage");
            previewImage.src = combineimage_url;
            callback();
        }
    };
    http.send(dataString);
}

var combineimage_url = null;