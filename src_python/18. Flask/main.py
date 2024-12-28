from flask import Flask,render_template

'''It creates the instance of the flask class 
which will be your WSGI (Web server gateway interface) application 
'''
app = Flask(__name__)


@app.route("/")
def Welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"


@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
