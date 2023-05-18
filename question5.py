#5. WAP to print first 5 number which is divided from 3 in given range 2001 to 2300
count=0
print("First 5 number which is divided from 3 in given range 2001 to 2300 : ")
for i in range(2001,2300):
    if(i%3==0):
        print(i,end=" ")
        count+=1
    if count==5:
        break