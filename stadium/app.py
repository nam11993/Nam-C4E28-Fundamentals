from flask import *
app = Flask(__name__)



@app.route("/")
def homepage():
    districts = ["Quận Hai Bà Trưng","Quận Thanh Xuân","Quận Cầu Giấy","Quận Nam Từ Liêm",]
    return render_template("homepage.html", districts = districts) 


    

if __name__ == '__main__':
    app.run(debug=True)