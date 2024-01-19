
# Flask Application Initialization
from flask import Flask, render_template, redirect, url_for

# Initialize the Flask Application
app = Flask(__name__)

# Define the Home Page Route
@app.route('/')
def home():
    """
    Renders the Home Page.

    Returns:
        HTML Template: The home page of the application, index.html.
    """

    return render_template('index.html')


# Define the Algorithms Page Route
@app.route('/algorithms')
def algorithms():
    """
    Renders the Algorithms Page.

    Returns:
        HTML Template: The algorithms page of the application, algorithms.html.
    """

    return render_template('algorithms.html')


# Define the Learn Page Route
@app.route('/learn')
def learn():
    """
    Renders the Learn Page.

    Returns:
        HTML Template: The learn page of the application, learn.html.
    """

    return render_template('learn.html')


# Define a Generic Error Handling Route
@app.errorhandler(404)
def page_not_found(error):
    """
    Handles Errors and Displays a Friendly Error Message.

    Args:
        error (Exception): The error that occurred.

    Returns:
        HTML Template: The error page template, error.html.
    """

    return render_template('error.html', error=error), 404


# Start the Flask Application
if __name__ == '__main__':
    app.run(debug=True)
