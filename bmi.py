def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


# Get user input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

# Output result
print(f"\nYour BMI is: {bmi:.2f}")
print(f"Category: {category}")