rowsize=int(input("Enter number of rows:"))

if rowsize%2==0:
    halfdiam=int(rowsize/2)
else:
    halfdiam=int(rowsize/2)+1
space=halfdiam-1
#loop for upper part
for i in range(1,halfdiam+1):#loop for rows
    for j in range(1,space+1):#loop for columns
        print(end=" ")
    space=space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
    #incrementing number at column
        num+=1
    print()
space=1
#loop for lower part
for i in range(1,halfdiam):#loop for rows
    for j in range(1,space+1):#loop for columns
        print(end=" ")
    space=space+1
    num=1
    for j in range(1,2*(halfdiam-i)):
        print(end=str(num))
        num+=1
    print()