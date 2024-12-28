from flask import Flask

'''It creates the instance of the flask class 
which will be your WSGI (Web server gateway interface) application 
'''
app = Flask(__name__)


@app.route("/")
def Welcome():
    return "Welcome to flask course This is amazing course and debug is on"


@app.route("/dash")
def dash():
    return "Welcome to the dash route buddy"



if __name__ == '__main__':
    app.run(debug=True)
