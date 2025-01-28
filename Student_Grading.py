def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 75:
        return 'B'
    elif percentage >= 50:
        return 'C'
    else:
        return 'Fail'

def calculate_results(name, marks):
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100
    grade = calculate_grade(percentage)
    return total_marks, percentage, grade

def student_grading_system():
    print("Welcome to the Student Grading System")

    name = input("Enter the student's name: ")

    marks = []
    for i in range(1, 6):
        mark = -1
        while mark < 0 or mark > 100:
            mark = float(input(f"Enter marks for subject {i} (out of 100): "))
            if mark < 0 or mark > 100:
                print("Invalid input. Please enter a mark between 0 and 100.")
        marks.append(mark)
    
    total_marks, percentage, grade = calculate_results(name, marks)
    
    print("\n---Student Results---")
    print(f"Name: {name}")
    print(f"Total Marks: {total_marks}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

student_grading_system()
