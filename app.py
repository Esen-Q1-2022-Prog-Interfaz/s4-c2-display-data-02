from crypt import methods
from flask import Flask, render_template, request
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


@app.route("/table/newPerson")
def newPerson():
    return render_template("newPerson.html")


# default de las routes es GET
@app.route("/table/insertNewPerson", methods=["POST"])
def insertNewPerson():
    if request.method == "POST":
        


if __name__ == "__main__":
    app.run(debug=True)
