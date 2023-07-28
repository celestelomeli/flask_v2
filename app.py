#This line imports three modules from the Flask package
#'Flask' is the class used to create Flask application instance
#'render_template' function allows you to render HTML templates from flask app
#'request' allows access to to incoming request data (i.e. POST)
from flask import Flask, render_template, request

#new instance of Flask class assigned to variable 'app'
#'__name__' = name of current Python module
app = Flask(__name__)

#route for root URL '/' that will execute 'index()' function
@app.route('/')
def index():
    return render_template('index.html')

#defines a route for URL '/greet' only for HTTP POST requests
#User submits form to greet URL function executes
#retrieving the value of 'name' field from form data and passing the 'name' variable to the template
@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return render_template('greet.html', name=name)

#Checks whether the script is run as main module and executes starting the Flask development server
#App accessible at default host and port 
if __name__ == '__main__':
    app.run()
