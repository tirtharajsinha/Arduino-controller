
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    send_from_directory,
    flash,
    make_response,
    jsonify,
    url_for,
    abort
)
from util import *


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("control.html")


@app.route('/sensor')
def sensordata():
    try:
        a, d = read_data()
        return {"status": 200, "angel": a, "dist": d}
    except:
        return {"status": 400}


@app.route('/runcommand', methods=["GET", "POST"])
def runcommand():
    thiscommand = request.args.get('command')
    print(thiscommand)
    try:
        send_command(thiscommand)
        return {"status": 200}
    except Exception as e:
        return {"status": 400}


# main driver function
if __name__ == '__main__':
    # app.run()
    app.run(host="0.0.0.0")
