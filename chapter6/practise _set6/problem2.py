'''write a program to find weather a student has passed or faied
if it requires a total of 40% and at least 33% in each subject to pass.
Assume 3 subjects and take marks as an input from the user.'''
marks1=int(input("Enter marks1:"))
marks2=int(input("Enter marks2:"))
marks3=int(input("Enter marks3:"))
 #check for total percentage
total_percantage= 100*(marks3+marks2+marks3)/300
if(total_percantage>=40 and marks1>33 and marks2>33 and marks3>33):
    print("YOU ARE PASSED")

else:
    print("YOU ARE FAILED!")