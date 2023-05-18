#reversing number
num=int(input("Enter number: "))
x=num
rev=0
while(num):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("reverse of ",x,"is",rev)
