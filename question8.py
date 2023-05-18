#8.WAP to count the vowel in your name.

name=input("Enter your name: ")
count=0
for i in name:
    if i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='O' or i=='o' or i=='u' or i=='U':
        count+=1
print("Number of vowels in",name,"is",count)

