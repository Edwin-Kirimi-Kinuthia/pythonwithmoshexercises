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



