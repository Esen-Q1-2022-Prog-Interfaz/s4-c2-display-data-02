from flask import Flask, render_template
from db import selectAllPersonData

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
    personList = selectAllPersonData()
    return render_template(
        "table.html",
        personList=personList,
    )


if __name__ == "__main__":
    app.run(debug=True)
