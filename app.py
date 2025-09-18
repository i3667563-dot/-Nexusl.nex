from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Секретный токен для доступа к админ-панели
SECRET_TOKEN = "your_secret_token_here"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/features")
def features():
    return render_template("features.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    # Обработка формы контактов
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    # Здесь можно добавить логику для отправки сообщения
    return redirect(url_for("contact"))

@app.route("/admin")
def admin():
    token = request.args.get("token")
    if token == SECRET_TOKEN:
        return render_template("admin.html")
    else:
        return "Unauthorized", 401

if __name__ == "__main__":
    app.run(port=9999, debug=True)


