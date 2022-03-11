from flask import Flask

app = Flask(__name__)


def bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


def italics(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


def underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper


@app.route("/")
@italics
@bold
@underline
def hello_world():
    return "<h1 style='color: red' align='center'>Hello, World!</h1>" \
           "<p style='color: blue' align='center'>This is a paragraph</p>" \
           "<img src='https://www.comfortzone.com/-/media/Images/ComfortZone-NA/US/Blog/bringing-new-kitten-home.jpg" \
           "?h=667&la=en&w=1000&hash=1B30399EA623982F3A1BCF8365A4864BB329CC70' " \
           "width='300'>" \
           "<img src='https://media3.giphy.com/media/aVPS1Ek7RhTtS/giphy.gif" \
           "?cid=790b7611866ab6c444bb5317b1bbd0ab3cfca5eb4062f2fb&rid=giphy.gif&ct=g'>"


@app.route("/bye")
def bye():
    pass


@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name} your age is {number}!"


if __name__ == "__main__":
    app.run(debug=True)
