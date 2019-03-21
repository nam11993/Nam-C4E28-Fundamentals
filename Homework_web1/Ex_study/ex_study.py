from flask import Flask, render_template, redirect
import os
app = Flask(__name__)


@app.route('/about-me')
def info():
    info = {
        "name": "Nam",
        "work": "QA_Tester",
        "school" : "HUBT",
        "gender" : "Male",
        "hobbies": "Football, Music"
        }
    return render_template('info.html', info = info)

@app.route('/school')
def school():
    return redirect("http://techkids.vn")


if __name__ == '__main__':
    app.run(debug=True)
 