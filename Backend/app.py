
from flask import Flask, render_template, request, redirect, url_for
from azure.storage.blob import BlobService
import base64
import time, datetime
import httplib
import urllib
import hashlib
import json
from facepp import API

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')


def generateImageUrl(request):
    account_name = "faceemoji"
    account_key = "kaoJiy0T7r6sXyo4wFYKCLgpAXbILKvkloeF+kFpCEUxC+bL9BxGA3WtofVxHcLPn3lMjw/UO/0sS1GCN3/AQw=="
    blob_service = BlobService(account_name, account_key)
    content = base64.b64decode(request.data)
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
    blob_name = hashlib.sha224(st).hexdigest() + 'image.png'
    blob_service.put_block_blob_from_bytes('image', blob_name, content)
    img_url = blob_service.make_blob_url('image', blob_name)
    print img_url
    return img_url

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/blob", methods=['POST'])
def handleBlob():
	img_url = generateImageUrl(request)
	ms_data = microsoftFaceAPI(img_url)
	fp_data = facePlusAPI(img_url)
	data = decideEmoji(fp_data, json.loads(ms_data))
	return json.dumps(data)


@app.route("/combine", methods=['POST'])
def handleCombine():
    return generateImageUrl(request)

@app.route("/post")
def post_on_fb():
  return render_template('post_on_fb.html')

def microsoftFaceAPI(url_str):
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
        json.dumps({"url": url_str}),
        headers
    )
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return data

def facePlusAPI(img_url):
	API_KEY = '0ef14fa726ce34d820c5a44e57fef470'
	API_SECRET = '4Y9YXOMSDvqu1Ompn9NSpNwWQFHs1hYD'
	api = API(API_KEY, API_SECRET)
	result = api.detection.detect(url = img_url)
	return result

def decideEmoji(fp_data, ms_data):
	emoji_list = []
	face_data = []
	url_prefix = "https://faceemoji.blob.core.windows.net/image/"
	print len(fp_data["face"])
	for i in range(0, min(len(fp_data["face"]), len(ms_data))):
		face = fp_data["face"][i]
		print ms_data
		ms_face = ms_data[i]
		print ms_face
		single_face = {
			"angle": ms_face["attributes"]["headPose"]["roll"],
			"width": ms_face["faceRectangle"]["width"],
			"height": ms_face["faceRectangle"]["height"],
			"left": ms_face["faceRectangle"]["left"],
			"top": ms_face["faceRectangle"]["top"]
		}
		face_data.append(single_face)
		keyword = ""
		if float(face["attribute"]["smiling"]["value"]) > 80:	
			face_attribute = face["attribute"]
			if "glass" in face_attribute:
				if face_attribute["glass"]["value"] != "None" and float(face_attribute["glass"]["confidence"]) > 80:
					keyword = "glass"
					continue
			if face_attribute["gender"]["value"] == "Male":
				keyword += "male"
			else:
				keyword += "female"

			print face_attribute["age"]
			if float(face_attribute["age"]["value"]) > 60:
				keyword += "_old"
			elif face_attribute["age"]["value"] < 30:
				keyword += "_young"
			else:
				keyword += "_middle"

			if float(face_attribute["race"]["confidence"]) > 80:
				if face_attribute["race"]["value"] == "Asian":				
					keyword += "_asian"
				elif face_attribute["race"]["value"] == "White":
					keyword += "_white"
				else:
					keyword += "_black"
			else:
				keyword = "smile"
			emoji_list.append(keyword)


	ret = {
		"face_data": face_data,
		"emoji_list": emoji_list
	}
	print emoji_list
	print face_data
	return ret		 

if __name__ == "__main__":
	app.debug = True
	app.run()

	

