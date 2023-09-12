from flask import Flask, render_template

app = Flask(__name__) 
@app.route('/')
def Home():
    return render_template("Homepage.html")

@app.route('/secondpage')
def Projeto1():
    return render_template("secondpage.html")

