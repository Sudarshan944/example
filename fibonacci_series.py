num=int(input("Enter number :"))
a,b=0,1
c=1
print(a,b,end=" ",sep=" ")
for i in range(num):
    c = a+b
    print(c, end=" ")
    a = b
    b = c