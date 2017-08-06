from flask import Flask, request, redirect, render_template, url_for


""" FOR SESSIONS AND USER HANDLING:
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

app.secret_key = "this ain't no time for doubting your power"
hashed_psw = generate_password_hash(psw) # to hash psw - ready to store
# to check saved and newly requested psw:
if check_password_hash(hashed_psw, new_psw): 
    session['username'] = username
"""

""" FOR API AND AJAX REQUEST HANDLING:
import requests
from flask import json, jsonify

return jsonify({"results": results, "status": status})
"""

app = Flask(__name__)


@app.route("/")
@app.route("/hello")
def hello():
    welcome = True
    return render_template("index.html", content=welcome)


@app.route("/bye")
def bye():
    return render_template("index.html")


@app.route("/tasks")
def tasks():
    return render_template("tasks.html")

# @app.route("/site", methods=['GET', 'POST'])

# request.args.get('form_name') - GET
# request.form['psw'] - POST

# return render_template("site.html", foo=foo) <- use to send something back
# return redirect("/index.html") <- use route here
# return url_for('hello') <- use function name here

if __name__ == '__main__':
    app.run(debug=True)
