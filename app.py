from flask import Flask, render_template, request, redirect, url_for
from db import selectAllPersonData, insertNewPerson
from Person import Person

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
@app.route("/table/createNewPerson", methods=["POST"])
def createNewPerson():
    if request.method == "POST":
        name = request.form.get("name")
        age = int(request.form.get("age"))
        salary = float(request.form.get("salary"))
        newPerson = Person(name, age, salary)
        print(newPerson)
        insertNewPerson(newPerson)
        return redirect(url_for("showTable"))


if __name__ == "__main__":
    app.run(debug=True)
