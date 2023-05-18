#6.WAP to skip to print those number which is divided from 7 between 301 to 400 
#Ex 1,2,3,4,5,6,8,9,10,11,12,13,15.......................................

for i in range(301,400):
    if(i%7==0):
        continue
    print(i,end=" ")