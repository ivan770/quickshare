from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import escape
from flask import redirect
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask import send_from_directory
from pathlib import Path
import string
import random 
app = Flask(__name__)
app.config.from_object('config')

csrf = CSRFProtect(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html',
                           error_text="404",
                           error_desc="Page not found"), 404

@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('error.html',
                           error_text="CSRF 0",
                           error_desc="CSRF security check didn't received entry token"), 400


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html',
                            error_text="500",
                           error_desc="Server is unable to process your request"), 500

@app.route('/')
def index():
    error = None
    error = request.args.get("error")
    if error is None:
        return render_template("index.html")
    elif error == "tooBigMessage":
        return render_template('index.html',
                                error="1")
    elif error == "tooSmallMessage":
        return render_template('index.html',
                                error="2")
    else:
        return render_template("index.html")

@app.route('/publish', methods=['GET', 'POST'])
def publish():
    message = None
    message = request.form.get("message")
    if message is None:
        return redirect("/?error=emptyMessage")
    length = len(message) - message.count(' ')
    if length > 150:
        return redirect("/?error=tooBigMessage")
    if length < 4:
        return redirect("/?error=tooSmallMessage")
    randomString = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    file = open("messages/" + randomString + ".txt", 'w')
    file.write(message)
    file.close()
    return redirect("/d/" + randomString)

@app.route('/d/<path:noteid>')
def noteFind(noteid):
    my_file = Path("messages/" + noteid + ".txt")
    if my_file.is_file():
        file = open("messages/" + noteid + ".txt", "r")
        message = file.read()
        file.close()
        return render_template('view.html',
                                message = message,
                                message_id = noteid)
    else:
        return render_template('error.html',
                           error_text="404",
                           error_desc="Message not found"), 404

@app.route('/f/<path:noteid>')
def fileFind(noteid):
    return send_from_directory("messages", noteid + ".txt", as_attachment=False)

if __name__ == '__main__':
    app.run()