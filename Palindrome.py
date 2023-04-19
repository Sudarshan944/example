num=int(input())
rev=0
temp=num
while num>0:
    rem=num%10
    rev=rev*10+rem
    num//=10
if(rev==temp):
    print("Palindrome")
else:
    print("Not a Palindrome")