from flask import Flask, request, redirect, render_template, url_for, session
import users
import tasks


""" FOR SESSIONS AND USER HANDLING:
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash


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
app.secret_key = "this ain't no time for doubting your power"


@app.route("/")
@app.route("/hello")
def hello():
    welcome = True
    return render_template("index.html", content=welcome)


@app.route("/bye")
def bye():
    return render_template("index.html")


@app.route("/project")
def test():
    return render_template("project.html")


@app.route("/login")
def set_session_data():
    session['username'] = "Jeannie"
    session['userid'] = 13
    counters = tasks.get_counters(13)
    session['task_counter'] = counters['task_count']
    session['project_counter'] = counters['project_count']
    session['team_counter'] = counters['team_count']
    return redirect("/tasks")


@app.route("/tasks")
def all_tasks_route():
    task_lists = tasks.all_tasks(session['userid'])
    return render_template("tasks.html", tasks=task_lists)

# @app.route("/site", methods=['GET', 'POST'])

# request.args.get('form_name') - GET
# request.form['psw'] - POST

# return render_template("site.html", foo=foo) <- use to send something to the jinja template
# return redirect("/index.html") <- use route here
# return url_for('hello') <- use function name here

if __name__ == '__main__':
    app.run(debug=True)
