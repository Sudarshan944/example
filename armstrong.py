num = input("Enter number :")
n = len(num)
num = int(num)
temp = num
sum = 0
while num > 0:
    rem = num % 10
    sum = sum+pow(rem, n)
    num //= 10
if (temp == sum):
    print("Armstrong")
else:
    print("Not Armstrong")
