number=int(input("Enter a number "))
add=0
for i in range (0,number):
    if i%3==0 or i%5==0:
       add=add+i
       i=i+1
print(add)
y=input("Press any key to exit")
    
