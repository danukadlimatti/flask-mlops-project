from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask is working! And its amazing web application and I am Enjoining doing it"

@app.route('/index')
def index():
    return "I have this index page inside the Flask file"


if __name__ == '__main__':
    app.run(debug=True)
