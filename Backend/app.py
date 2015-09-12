from flask import Flask, render_template, request
from azure.storage.blob import BlobService
import base64
import time, datetime
import httplib
import urllib
import json

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/blob", methods=['POST'])
def handleBlob():
    account_name = "faceemoji"
    account_key = "kaoJiy0T7r6sXyo4wFYKCLgpAXbILKvkloeF+kFpCEUxC+bL9BxGA3WtofVxHcLPn3lMjw/UO/0sS1GCN3/AQw=="
    blob_service = BlobService(account_name, account_key)
    content = base64.b64decode(request.data)
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
    blob_name = st + 'image.png'
    blob_service.put_block_blob_from_bytes('image', blob_name, content)
    result = blob_service.get_blob_metadata('image', blob_name)
    print blob_service.make_blob_url('image', blob_name)
    return "Success"

@app.route("/post")
def post_on_fb():
  return render_template('post_on_fb.html')


@app.route("/analytics", methods=['POST'])
def handleFaceAnaylitics():
    json_data = json.loads(request.data)
    single_data = json_data[0]
    attributes = single_data['attributes']
    print attributes['gender']
    return "Success"


@app.route("/test")
def test():
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": "f4f23db3a4e244779bfa3f01bd6f89ca"
    }
    conn = httplib.HTTPSConnection("api.projectoxford.ai")
    params = urllib.urlencode({
        "analyzesFaceLandmarks": "true",
        "analyzesAge": "true",
        "analyzesGender": "true",
        "analyzesHeadPose": "true"
    })
    conn.request(
        "POST",
        "/face/v0/detections?%s" % params,
        json.dumps({"url": "https://faceemoji.blob.core.windows.net/image/photo.png"}),
        headers
    )
    response = conn.getresponse()
    data = response.read()
    print data
    conn.close()
    return "test"

if __name__ == "__main__":
	app.debug = True
	app.run()

