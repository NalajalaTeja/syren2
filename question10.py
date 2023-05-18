#10. WAP to find that max number among 3 number .

num1=int(input("Enter number1: "))
num2=int(input("Enter number2: "))
num3=int(input("Enter number3: "))

if(num1>num2 and num1>num3):
    print(num1,"is largest among",num1,",",num2,",",num3)
elif(num2>num3):
    print(num2,"is largest among",num1,",",num2,",",num3)
else:
    print(num3,"is largest among",num1,",",num2,",",num3)