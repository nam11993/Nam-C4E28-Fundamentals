from flask import Flask, render_template, redirect, request, session
from services import services
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["SECRET_KEY"] = "fj39#@32F><@#.f3fe:#$P3"


@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/all-service')
def all_service():
    if session["logged"]:
        service = services.find()
        return render_template('all_service.html', service = service)
    else:
        return redirect("/login")

# @app.route('/all-service/male')
# def male():
#     male = services.find({"gender": "male"})
#     return render_template('male.html', male = male)

# @app.route('/all-service/female')
# def female():
#     female = services.find({"gender": "female"})
#     return render_template('female.html', female = female)

@app.route('/all-service/<gender>')
def male_service(gender):
    service = services.find({"gender": gender})
    return render_template('all_service.html', service = service)

@app.route('/all-service/detail/<id>/')
def details(id):
    detail_service = services.find_one({"_id": ObjectId(id)})
    return render_template("detail_service.html", detail_service = detail_service)
    
@app.route("/delete/<id>")
def delete(id):
    delete_service = services.find_one({"_id": ObjectId(id)})
    if delete_service is not None:
        services.delete_one(delete_service)
    else:
        return "Not found service"
    return redirect("/all-service")

@app.route("/update/<id>", methods = ["GET","POST"])
def update(id):
    edit_service = services.find_one({"_id": ObjectId(id)})
    if request.method == "GET":
        return render_template("update_service.html", edit_service = edit_service)
    elif request.method == "POST":
        form = request.form
        name = form["full_name"]
        age = form["age"]
        address = form["address"]
        gender = form["gender"]
        available = form["available"]
        new_value = { "$set": { 
            "name": name,
            "age": age,
            "address": address,
            "gender": gender,
            "available": available,
        }}
        services.update_one(edit_service, new_value)
        return redirect("/all-service/detail/{0}/".format(id))


@app.route("/login", methods = ["GET","POST"])
def login():
    if not session["logged"]: #chua dang nhap
        if request.method == "GET":
            return render_template("login.html")
        elif request.method == "POST":
            form = request.form
            username = form["username"]
            password = form["password"]
            if username == "adminc4e" and password == "adminc4e":
                session["logged"] = True
                return redirect("/all-service")
            else:
                return redirect("/login")
    else: #dang nhap roi
        return redirect("/all-service")


@app.route("/logout")
def logout():
    del session["logged"]  #c1
    session["logged"] = False #c2
    return redirect("/login")






if __name__ == '__main__':
    app.run(debug=True)
