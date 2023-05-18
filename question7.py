#7. WAP to calculate factorial in given format
#print : 4! = 4.3.2.1=24
num=int(input("Enter number: "))
print(str(num)+"! =",end=" ")
mul=1
for i in range(num,1,-1):
    print(i,end=".")
    mul=mul*i
print("1=",mul)
