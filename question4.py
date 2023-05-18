num=int(input("Enter number: "))
x=num
l=len(str(num))
amst=0
while(num):
    rem=num%10
    amst+=pow(rem,l)
    num=num//10
if(amst==x):
    print(x," is an Amstrong numbers")
else:
    print(x,"not an Amstrong numbers")