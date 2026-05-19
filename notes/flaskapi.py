
from flask import Flask

app = Flask(__name__)
# print(__name__) #this will print __main__

@app.route("/") #route decorator => A route connects a URL to a Python function.
def home():
    return "Hello"

app.run() #start the flask server
#it is same as => app.run(host="127.0.0.1", port=5000)


#another example
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

@app.route("/about")
def about():
    return "About Page"

@app.route("/contact")
def contact():
    return "Contact Page"

app.run()