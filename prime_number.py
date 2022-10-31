number = int(input("Enter a number: "))

isPrime = False

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            isPrime = True
            break

if isPrime:
    print(number, "is not a prime number")
else:
    print(number, "is a prime number")
