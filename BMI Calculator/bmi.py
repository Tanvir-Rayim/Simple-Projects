height = input("Enter your height in meters: ")
weight = input("Enter your weight in kilograms: ")

bmi = float(weight) / (float(height) ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}, you are underweight.")
elif 18.5 <= bmi < 25:
    print(f"Your BMI is {bmi:.2f}, you have a normal weight.")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi:.2f}, you are overweight.")
else:
    print(f"Your BMI is {bmi:.2f}, you are obese.")
