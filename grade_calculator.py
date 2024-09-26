# Input from the user

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

# Grade calculation 

lab_weigh = int(lab_problems * 20/6) 
activity_weigh = int(quizzes_or_in_class_activities * 15/6)

overall_grade = ((int(lab_weigh + activity_weigh + (assignment_1 + assignment_2 + assignment_3 + assignment_4) * 16 + (midterm_1 + midterm_2) * 25 + final_exam * 18 + midterms_and_final_prep * 6)) / 100)

print("Your grade is: ", overall_grade)
