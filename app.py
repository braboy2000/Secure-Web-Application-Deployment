from flask import Flask

#creates app
app = Flask(__name__)


#sets up a URL route
@app.route('/')
def home():
    return "Hello, World version2!"

if __name__ == "__main__":
    app.run(debug=True)