from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    name = "pedro"
    showParagraph = True
    return render_template(
        "home.html",
        name=name,
        showParagraph=showParagraph,
    )


if __name__ == "__main__":
    app.run(debug=True)
