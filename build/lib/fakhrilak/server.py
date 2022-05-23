from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



def main():
    app.run(debug=True,host='0.0.0.0', port=5002)