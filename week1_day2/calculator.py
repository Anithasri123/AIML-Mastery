def add(a,b):
    return a+b
def sub(a,b):
    return a-b 
def mul(a,b):
    return a*b 
def div(a,b):
    return a/b 

while(True):
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    option=int(input("Choose an option:"))
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    if option==1:
        res=add(a,b)
        print(res)
    elif option==2:
        res=sub(a,b)
        print(res)
    elif option==3:
        res=mul(a,b)
        print(res)
    elif option==4:
        if b==0:
            print("Denominator can't be zero")
        else:
            res=div(a,b)
            print(res)
    else:
        print("Enter valid option")
    