from flask import Flask,render_template
import sqlite3

app = Flask(__name__)
db_contact = sqlite3.connect('texpo.db')
cursor = db_contact.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/another')
def second():
    return render_template('another.html')

@app.route("/search")
def search():
    renderpage = render_template("search.html")
    return renderpage

# @app.route("/search_result",methods = ["POST"])
# def search_result():

    
    
@app.route('/upload', method=["GET", "POST"])
def upload():
    cursor.execute = ("INSERT INTO post (title, sport, content) VALUES (?, ?, ?)", 
                  request.form.get("title"), request.form.get("sport"), request.form.get("content"))
    return redirect("/")
    
app.debug =  True
app.run()