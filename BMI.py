#BMI CONSTANTS
UNDER = 18.5
HEALTHY = 24.9
OVERWEIGHT = 29.9

#QUESTIONS
name = input("Enter name")
weight = float(input("Enter weight"))
height = float(input("Enter Height"))

#calculations
category = "unknown"
if (weight > 0 and height > 0):
    bmi = weight / (height ** 2)
    if bmi < UNDER:
        category = "UNDER"
    elif bmi <= HEALTHY:
        category = "HEALTHY"
    elif bmi <=OVERWEIGHT:
        category = "OVERWEIGHT"
    else:
        category = "OBESE"
        
    print (f"Hi, {name}! Your BMI is {bmi} and that results as {category} ")
else:
    print ("your height and weight should be above 0'")
    