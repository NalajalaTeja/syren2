#5. WAP to print first 5 number which is divided from 3 in given range 2001 to 2300
count=0
num1=int(input("Enter the stating range: "))
num2=int(input("ENter the ending range: "))
print("First 5 number which is divided from 3 in given range",num1,"to", num2," : ")
for i in range(num1,num2):
    if(i%3==0):
        print(i,end=" ")
        count+=1
    if count==5:
        break