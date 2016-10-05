from flask import Flask, render_template
app = Flask(__name__)

#creating the home page - first visit website page
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

#we've created the app, but we haven't run it yet. 
#8 lines of code has created an app!
#adding debut = true allows you to change the code without 
#having to rerunning it every time.
app.run(debug=True)