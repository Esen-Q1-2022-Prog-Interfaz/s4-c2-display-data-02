from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    name_backend = "balbino"
    return render_template("home.html", name_frontend=name_backend)


if __name__ == "__main__":
    app.run(debug=True)
