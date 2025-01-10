def greatest():
    
    a=int(input("Enter you number"))
    b=int(input("Enter you number"))
    c=int(input("Enter you number"))
    if(a>b and a>c):
        print(" a is greatest")
    elif(b>c and b>a):
        print("b is greatest")
    else:
        print("c is greatest")
greatest()