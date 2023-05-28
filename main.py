
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    """
    Webserver entry point
    """
    return "Hello, World! - vaidya -- "
    
if __name__ == "__main__":
    app.run(debug=True)