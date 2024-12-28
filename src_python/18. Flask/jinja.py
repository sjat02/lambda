#building URL dynamically 
#jinja 2 template engine 
#variable rule 

#jinja 2 template engine there are multiple source to read the data from html page 
'''
{{ }} this are expression to print output in html
{%...%} conidtion for loop
{#...#} this is for comments

'''



from flask import Flask,render_template,request
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')


#variable rule
@app.route('/success/<int:score>')
def success(score):
    res=''
    if score>=50:
        res='PASSED'
    else:
        res='FAILED'

    return render_template('result.html',results=res)




@app.route('/successres/<int:score>')
def successres(score):
    res=''
    if score>=50:
        res='PASSED'
    else:
        res='FAILED'
    
    exp={'score':score,'res':res}

    return render_template('result1.html',results=exp)




if __name__=="__main__":
    app.run(debug=True)