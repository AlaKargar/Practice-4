n = int(input("Enter the number of Fibonacci series: "))

fibonacci = [1, 1]


for i in range(2, n):
    number = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(number)

print(fibonacci)
