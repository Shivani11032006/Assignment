def calculate_grade():
    try:
        # Taking input for marks in three subjects
        subject1 = float(input("Enter marks for Subject 1: "))
        subject2 = float(input("Enter marks for Subject 2: "))
        subject3 = float(input("Enter marks for Subject 3: "))

        # Calculating the average
        average = (subject1 + subject2 + subject3) / 3

        # Determining the grade
        if average >= 90:
            grade = "A"
        elif 80 <= average < 90:
            grade = "B"
        elif 70 <= average < 80:
            grade = "C"
        else:
            grade = "Fail"

        # Printing the result
        print(f"Average Marks: {average:.2f}")
        print(f"Grade: {grade}")
    except ValueError:
        print("Invalid input! Please enter numeric values for marks.")

# Call the function
calculate_grade()