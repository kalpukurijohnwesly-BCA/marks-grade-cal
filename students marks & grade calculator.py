# Student Marks & Grade Calculator

def calculate_grade(marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"

    return total, average, grade


# Input from user
marks = []
num_subjects = int(input("Enter number of subjects: "))

for i in range(num_subjects):
    score = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(score)

# Function call
total, avg, grade = calculate_grade(marks)

# Output
print("\n--- Report Card ---")
print("Marks:", marks)
print("Total:", total)
print("Average:", avg)
print("Grade:", grade)