n1=int(input())
n2=int(input())
n3=int(input())
if n1>n2 and n1>n3:
    if n2<n3:
        temp=n1
        n1,n2=n2,n3
        n3=temp
    else:
        temp = n1
        n1=n3
        n3 = temp
elif n1<n3:   ###STILL PENDIND
    if n2<n3:
        print(n2,n1,n3)
    else:
        print(n1,n3,n2)
else:
    if n2>n3:
        print(n3,n2,n1)
    else:
        print(n2,n3,n1)