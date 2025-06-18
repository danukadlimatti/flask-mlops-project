from flask import Flask
'''
It creates an instance of flask class,
which will be a WSGI application
'''
## WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask Course, this is an amazing course"


if __name__=="__main__":
    app.run()
