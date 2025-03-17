print("Your Menu is:\n1.Addition\n2.Subtraction\n3.Multiplication")
option = int(input("Enter your option : "))

if(option==1):
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))
    print(f"Addition : {a}+{b}=",a+b)
elif(option==2):
    n1 = int(input("Enter First Number : "))
    n2 = int(input("Enter Second Number : "))
    print(f"Subtraction = {n1}-{n2}=",n1-n2)
elif(option==3):
    num1 = int(input("Enter First Number : "))
    num2  = int(input("Enter Second Number : "))
    print(f"Multiplication : {num1}*{num2}=",num1*num2)
