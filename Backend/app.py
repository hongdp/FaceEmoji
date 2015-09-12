from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
  return render_template('index.html')

@app.route("/post_on_fb")
def post_on_fb():
  return render_template('post_on_fb.html')

if __name__ == "__main__":
    app.run()

