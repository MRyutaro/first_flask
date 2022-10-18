from flask import Flask, render_template, request
from datebase_operation import UserData

app = Flask(__name__)
user_data = UserData("user_info.db", "userinfo")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/try_signup", methods=["POST"])
def try_signup():
    email = str(request.form.get("email"))
    username = str(request.form.get("username"))
    password = int(request.form.get("password"))
    # emailがあるかチェック
    user_data.add_user(email, username, password)
    return render_template("complete_signup.html", email=email, username=username, password=password)


if __name__ == "__main__":
    app.run(debug=True)
