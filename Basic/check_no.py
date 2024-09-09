class check_number:
    def __init__(self, number):
        self.number = number

    def isPrime(self):
        if self.number < 2:
            return False
        for i in range(2, int(self.number ** 0.5) + 1):
            if self.number % i == 0:
                return False
        return True
    
    def Even_odd(self):
        return self.number % 2 == 0
        
    def armstrong(self):
        num = self.number
        sum = 0
        original_num = num
        while num != 0:
            rem = num % 10
            sum += rem ** 3
            num = num // 10
        return sum == original_num
    
    def is_palindrome(self):
        number = self.number
        original_number = self.number
        reversed_number = 0

        while number > 0:
            digit = number % 10
            reversed_number = reversed_number * 10 + digit
            number = number // 10

        return original_number == reversed_number

    def Fibonacci(self):
        n = self.number
        if n < 0:
            return "Incorrect input"
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b
        
    def factorial(self):
        def recursive_factorial(n):
            if n == 0:
                return 1
            return n * recursive_factorial(n - 1)

        return recursive_factorial(self.number)


def main():
    num = int(input("ENter No for Full Checking: "))
    check = check_number(num)
    
    if check.isPrime():
        print(f"The given number {num} is prime.")
    else:
        print(f"The given number {num} is NOT prime.")

    if check.Even_odd():
        print(f"The given number {num} is Even.")
    else:
        print(f"The given number {num} is Odd.")

    if check.armstrong():
        print(f"The given number {num} is an Armstrong number.")
    else:
        print(f"The given number {num} is NOT an Armstrong number.")

    if check.is_palindrome():
        print(f"The given number {num} is a palindrome.")
    else:
        print(f"The given number {num} is NOT a palindrome.")

    if num < 30:
        fib_value = check.Fibonacci() 
        print(f"Fibonacci of {num} is {fib_value}")
    else:
        print('Number is too big for Fibonacci')

    if num < 20:
            fac_value = check.factorial() 
            print(f"Factorial of {num} is {fac_value}")
    else:
            print('Number is too big for Factorial')


if __name__ == "__main__":
    main()
