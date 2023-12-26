from flash import Flask

app = Flask(__name)

@app.route("/")
def hello():
    return "Hello, World!"

