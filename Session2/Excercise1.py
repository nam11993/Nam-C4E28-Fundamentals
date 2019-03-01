hei = int(input("height(cm): "))
wei = float(input("weight(kg): "))
heim = hei *0.01
BMI = wei / heim**2
print (BMI)

if BMI < 16:
    print("Severely underweight")
elif BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")