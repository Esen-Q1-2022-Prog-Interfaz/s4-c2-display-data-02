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
    return render_template("table.html")


if __name__ == "__main__":
    app.run(debug=True)
