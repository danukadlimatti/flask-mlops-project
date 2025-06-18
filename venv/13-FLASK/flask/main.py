from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<html><h1>Welcome to Flask course</h1></html>"

@app.route('/index')
def index():
    return "I have this index page inside the Flask file"

if __name__ == '__main__':
    app.run(debug=True)
