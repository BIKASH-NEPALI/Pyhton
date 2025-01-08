# write a program to find the greatest number entered by the user.
a=int(input("Enter number1:"))
b=int(input("Enter number2:"))
c=int(input("Enter number3:"))
d=int(input("Enter number4:"))

if(a>b and a>c and a>d):
    print("a is greatest")
elif(b>a and b>c and b>d):
    print("b is gratest")
    
elif(c>a and c>b and c>d):
    print("c is greatest")
else:
    print("d is greatest number")
