from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return "<html><h1>Welcome to Flask course</h1></html>"

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name} '
    return render_template('form.html')



@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name} '
    return render_template('form.html')



@app.route('/', methods=['GET'])
def index():
    return '''
        <h2>Welcome!</h2>
        <form method="POST" action="/greet">
            Name: <input type="text" name="name">
            <input type="submit" value="Greet me">
        </form>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f"<h2>Hello, {name}!</h2>"



if __name__ == '__main__':
    app.run(debug=True)
