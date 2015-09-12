from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/blob", methods=['POST'])
def handleBlob():
    print(request.data)
    return "Success"

if __name__ == "__main__":
	app.debug = True
	app.run()

