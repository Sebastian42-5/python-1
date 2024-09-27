# User input

lab_problems = int(input("Enter the number of labs completed: "))
quizzes_or_in_class_activities = int(input("Enter the number of quizzes completed: "))
assignment_1 = int(input("Enter grade for Assignment 1: "))
assignment_2 = int(input("Enter grade for Assignment 2: "))
assignment_3 = int(input("Enter grade for Assignment 3: "))
assignment_4 = int(input("Enter grade for Assignment 4: "))
midterm_1 = int(input("Enter grade for Midterm 1: "))
midterm_2 = int(input("Enter grade for Midterm 2: "))
final_exam = int(input("Enter grade for Final Exam: "))
midterms_and_final_prep = int(input("Enter grade for Midterms and Final Preparation: "))

# Calculations  

if lab_problems > 6: 
    lab_percent = 100
else:
    lab_percent = int(lab_problems * 100/6) 

if quizzes_or_in_class_activities > 6:
    activity_percent = 100
else:
    activity_percent = int(quizzes_or_in_class_activities * 100/6)

overall_grade = int(((lab_percent * 20) + (activity_percent * 15) + (assignment_1 * 4) + (assignment_2 * 4) + (assignment_3 * 4) + (assignment_4 * 4) + (midterm_1 * 12.5) + (midterm_2 * 12.5) + (final_exam * 18) + (midterms_and_final_prep * 6)) / 100)

print("Your grade is: ", overall_grade)
