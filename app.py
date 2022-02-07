from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    name = "pedro"
    showParagraph = True
    dayOfWeek = 100
    numberList = ["bombom", "bellota", "burbuja"]
    return render_template(
        "home.html",
        name=name,
        showParagraph=showParagraph,
        dayOfWeek=dayOfWeek,
        numberList=numberList,
    )


@app.route("/table")
def showTable():
    personList = [
        {
            "name": "balbino",
            "age": 23,
            "salary": 300.0,
        },
        {
            "name": "rod",
            "age": 25,
            "salary": 450.0,
        },
        {
            "name": "gaby",
            "age": 28,
            "salary": 650.0,
        },
    ]

    """ personList = [] """
    return render_template(
        "table.html",
        personList=personList,
    )


if __name__ == "__main__":
    app.run(debug=True)
