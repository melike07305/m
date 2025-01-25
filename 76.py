def factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1,n + 1):
            result *= i 
        return result
    
try:
    num = int(input("Enter a number: "))
    fact = factorial(num)
    print("Factorial of", num, "is", fact)

except ValueError:
    print("Error: Invalid input. please eneter  a positive number.")

