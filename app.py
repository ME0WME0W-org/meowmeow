from flask import Flask, request, session, render_template, render_template_string, redirect
from time import time
app = Flask(__name__)
app.config['SECRET_KEY'] = "4ik1uLm6VTZbkSg0Op2wx5dIqF1GoR39frNng8gqtggK"

@app.route('/')
def home():
    if "user" in session:
        return render_template("cat.html", user=session.get("user"), time=time())    
    return render_template("login.html")

@app.route('/nyan')
def nyan():
    if session.get("vip"):
        return render_template_string("""
<form><input name="say" placeholder="cat say..."></form>
<img src="https://cataas.com/cat/cute/says/{}">
""".format(request.args.get("say","MEOW")))
        # return render_template("nyan.html")
    return redirect("/")

@app.route('/login', methods=["POST"])
def login():
    session["user"] = request.values['username']
    session["vip"] = False
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)