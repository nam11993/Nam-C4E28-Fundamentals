from flask import *
from data import bikes
app = Flask(__name__)

@app.route("/submit")
def submit():
    return render_template("submit.html")

@app.route("/new_bike",methods = ["GET","POST"])
def new_bike():
    if request.method == "GET":
        return render_template("bike_rental_service.html")
    elif request.method == "POST":
        form = request.form
        model = form["model"]
        daily_fee = form["daily_fee"]
        image = form["image"]
        year = form["year"]
        new_bike = {
            "model": model,
            "daily_fee": daily_fee,
            "image": image,
            "year": year,
        }
        bikes.insert_one(new_bike)
        return redirect("/new_bike")                             
    

if __name__ == '__main__':
    app.run(debug=True)