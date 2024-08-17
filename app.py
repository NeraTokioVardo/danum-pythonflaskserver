from flask import Flask

app = Flask("My Flask Application")


@app.route("/")
def hello():
    return "<h1>Hello World from my fork!</h1>"

@app.route("/goodbye")
def hello():
    return "<h1>Goodbye from my app!</h1>"


if __name__=="__main__":
    app.run(debug=True) 
    # When no port is specified, starts at default port 5000
