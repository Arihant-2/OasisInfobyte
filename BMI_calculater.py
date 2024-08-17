import argparse

# BMI, Body Mass Index

# Function to calculate BMI and determine the category
def calculate_bmi(weight, height):
    # Calculate BMI
    bmi = weight / (height**2)

    # Determine the category based on BMI value
    if bmi < 18.5:
        state = "Underweight state"
    elif 18.5 <= bmi < 24.9:
        state = "Normal weight state"
    elif 25.0 <= bmi < 29.9:
        state = "Overweight state"
    else:
        state = "Obesity state"

    return bmi, state

# -----------------------------------------------------------------------------------------------------------
# Interaction with user
#-------------------------------------------------------------------------------------------------------------

def main():
    # Ask for the user's weight and height
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        # Check if weight and height are positive
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values !")
            return

        # Calculate BMI and determine the category
        bmi, state = calculate_bmi(weight, height)

        # Display the result to the user
        print(f"Your BMI is: {bmi:.4f}")
        print(f"According your BMI, you are in : {state}")

    except ValueError:
        # Handle invalid input (non-numeric values)
        print("Please enter valid numbers for weight and height.")


# Entry point for the script
if __name__ == "__main__":
    main()
