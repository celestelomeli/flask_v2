# Flask: Main class for creating the web application
# render_template: Renders HTML templates with dynamic data
# request: Accesses incoming HTTP request data (forms, query params, etc.)
from flask import Flask, render_template, request

# Create Flask application instance
app = Flask(__name__)

# Route for home page
@app.route('/')
def index():
    """Render the home page with name input form."""
    return render_template('index.html')

# Route for form submission (POST only)
@app.route('/greet', methods=['POST'])
def greet():
    """Process form submission and display personalized greeting."""
    # Get 'name' value from submitted form data
    name = request.form['name']
    # Pass name variable to template for rendering
    return render_template('greet.html', name=name)

# Run the Flask development server
if __name__ == '__main__':
    # debug=True enables auto-reload and detailed error messages
    app.run(debug=True)
