def bmi(weight, height):
    bmi = (weight / (height ** 2))
    print(bmi)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    elif bmi > 30:
        return "Obese"

print(bmi(50, 1.80))