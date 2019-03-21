from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmiwithoutrender/<int:weight>/<int:height>')
def bmi1(weight, height):
    bmi = weight/((height/100)**2)
    if(bmi < 16):
        result = "Severely underweight"
    elif(bmi < 18.5):
        result = "Underweight"
    elif(bmi < 25):
        result = "Normal"
    elif(bmi < 30):
        result = "Overweight"
    else:
        result = "Obese"
    return " This is your Body Mass Index: {0} and your conditional : {1}".format((str(bmi)),result)

@app.route('/bmiwithrender/<int:weight>/<int:height>')
def bmi2(weight, height):
    bmi = weight/((height/100)**2)
    if(bmi < 16):
        result = "Severely underweight"
    elif(bmi < 18.5):
        result = "Underweight"
    elif(bmi < 25):
        result = "Normal"
    elif(bmi < 30):
        result = "Overweight"
    else:
        result = "Obese"
    return render_template("bmi.html", bmi = bmi, result = result)

if __name__ == '__main__':
    app.run(debug=True)
 