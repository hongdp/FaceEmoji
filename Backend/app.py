from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/blob", methods=['POST'])
def handleBlob():
    print(request.data)
    return "Success"

@app.route('/REST', methods=['POST'])
def create_task():
    print("hello")
    return request.data, 200

if __name__ == "__main__":
	app.debug = True
	app.run()

