from flask import *
app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def homepage():
    if request.method == "GET":
        return render_template("homepage.html")
    elif request.method == "POST":
        return redirect("san-bong.html")

@app.route("/san-bong")
def sanbong():
    districts = ["Hà Nội (10)","Quận Hai Bà Trưng (3)","Quận Thanh Xuân (3)","Quận Cầu Giấy (2)","Quận Nam Từ Liêm (2)",]
    return render_template("san-bong.html", districts = districts) 

@app.route("/san-bong/san-bong-hai-ba-trung")
def haibatrung(): 
    return render_template("san-bong-hai-ba-trung.html")

@app.route("/san-bong/san-bong-thanh-xuan")
def thanhxuan(): 
    return render_template("san-bong.html")   

@app.route("/san-bong/san-bong-cau-giay")
def caugiay(): 
    return render_template("san-bong.html") 

@app.route("/san-bong/san-bong-nam-tu-liem")
def namtuliem(): 
    return render_template("san-bong.html") 
    

if __name__ == '__main__':
    app.run(debug=True)