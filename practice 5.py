num1 = int(input("please enter the first num: "))
num2 = int(input("please enter the second num: "))

if num1 > num2:
    min = num2
else:
    min = num1

gcd = 1
for i in range(1, min+1):
    if (num1 % i == 0) and (num2 % i == 0):
        gcd = i

print("your gcd is: ", gcd)
