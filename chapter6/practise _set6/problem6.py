# A program to calculate grade of students from his marks:
marks_obtained=int(input("Enter your marks:"))
if(marks_obtained<=100 and marks_obtained>=90):
    grade="A+"
elif(marks_obtained<90 and marks_obtained>=80):
    grade="A"
elif(marks_obtained<80 and marks_obtained>=70):
    grade="B+"
elif(marks_obtained<70 and marks_obtained>60):
    grade="B"
print("your grade is:", grade)