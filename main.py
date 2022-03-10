from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Rule Hello, World!"

@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name} your age is {number}!"


if __name__ == "__main__":
    app.run(debug=True)
