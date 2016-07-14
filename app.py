from flask import Flask, redirect, render_template
import re
app = Flask(__name__)


def logger(owerName, money):
    logOutput = owerName + ";" + money

    with open("logfile.log", "a") as logfile:
        logfile.write(logOutput + "\n")

    return "Writing to Log" + logOutput


@app.route("/")
def usage():
    return render_template('usage.html')

@app.route("/<owerName>/<money>")
def core(owerName, money):

    if not re.match("^[a-zA-Z]+$", owerName):
        return render_template('errpage.html'), 500
    if not re.match("^[0-9]+$", money):
        return render_template('errpage.html'), 500

    logger(owerName, money)

    return render_template('fade2.html', owerName=owerName.title(), money=money)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
