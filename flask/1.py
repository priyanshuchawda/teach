# If not already installed, install Flask using: pip install Flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

app.run()
