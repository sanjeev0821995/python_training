for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()

for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()

temp=1
for i in range(1,6):
    for j in range(i):
        print(temp,end="")
        temp=temp+1
    print()

for n in range(1,100):
    if n%2==0:print(n,end=" ")