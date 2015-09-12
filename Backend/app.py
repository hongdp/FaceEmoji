from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/blob", methods=['POST'])
def handleBlob():
    print(request.data)
    return "Success"

@app.route('/save', methods=['POST', 'GET'])
def saveImage():
	if request.method == 'POST':
		print "s"


if __name__ == "__main__":
	app.debug = True
	app.run()

