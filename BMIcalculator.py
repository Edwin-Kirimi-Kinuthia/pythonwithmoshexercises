def convert_height(height, unit_height):
    try:
        height = float(height)
        if height < 0:
            raise ValueError("Height cannot be negative!")

        if unit_height == 'cm':
            converted_height = height * 0.01
        elif unit_height == "ft":
            converted_height = height * 0.3048
        elif unit_height == "m":
            converted_height = height
        else:
            raise ValueError("Use correct units; cm, m, or ft")

        return converted_height

    except ValueError as e:
        return f"Error: {e}"


def convert_weight(weight, unit_weight):
    try:
        weight = float(weight)
        if weight < 0:
            raise ValueError("Weight cannot be negative!")

        if unit_weight == "kg":
            converted_weight = weight
        elif unit_weight == "lb":
            converted_weight = weight * 0.453592
        else:
            raise ValueError("Use correct units; kg or lb")

        return converted_weight

    except ValueError as e:
        return f"Error: {e}"


# Input handling
height = input('Height: ')
unit_height = input("Unit (cm for centimeters, m for metres, and ft for feet): ").lower()
weight = input("Your weight: ")
unit_weight = input("Unit (kg for kilograms or lb for pounds): ").lower()

# Convert height and weight
height_for_bmi = convert_height(height, unit_height)
weight_for_bmi = convert_weight(weight, unit_weight)

# Calculate and print BMI
if isinstance(height_for_bmi, float) and isinstance(weight_for_bmi, float):
    bmi = weight_for_bmi / (height_for_bmi ** 2)
    print(f"Your BMI is {bmi:.2f}")
else:
    if isinstance(height_for_bmi, str):
        print(height_for_bmi)
    if isinstance(weight_for_bmi, str):
        print(weight_for_bmi)
