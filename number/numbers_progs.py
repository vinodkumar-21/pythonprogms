#prog for fibonacci series
def getFibonacci(n):
    fibo = [0, 1]

    for i in range(2, n):
        fibo.append(fibo[i-2] + fibo[i-1])
    return fibo

print(getFibonacci(10))


#prog for factorial and it is alos for recursive call itself
def getFactorial(n):
    if n == 0:
        return 1
    return n * getFactorial(n - 1)

print(getFactorial(5))


# prog for even and odd 
def getEvenOdd(n):
    return "even no" if n % 2 == 0 else "odd no"

print(getEvenOdd(10))


#prog print table no
def getTable(n):
    output =""
    for i in range(1, 11):
        result = n * i
        output += f"{n} x {i} = {result}\n"
    return output

print(getTable(5))

# prog print armstrong no using number convert into string
def getArmstrong(num):
    digits = str(num)
    n = len(digits)
    sum = 0

    for digit in digits:
        sum = sum + int(digit) ** n
    return "armstrong no" if num == sum else "not armstrong no"

print(getArmstrong(153))

#prog print armstrong without converting string
import math
def getArmstrongNumber(num):
    sum = 0
    orig = num
    length = 1 if num == 0 else int(math.log10(num) + 1)

    while num > 0:
        digit = num % 10
        sum = sum + int(digit) **length
        num = num // 10
    return "armstrong no" if orig == sum else "not armstrong no"

print(getArmstrongNumber(111111))


#prog for palindrome number
def getPalindromeNumber(num):
    orig = num
    reverse = 0

    while num > 0:
        digit = num % 10   
        reverse = reverse * 10 + digit
        num = num // 10
    return "palindrome number" if orig == reverse else "not palindrome number"

print(getPalindromeNumber(121))


#prog for palindrome string
def getPalindromeString(str):
    orig = str
    reverse = ""

    for i in range(len(str) -1, -1, -1):
        reverse += str[i]
    return "palindrome string" if reverse == orig else "not palindrome string"

print(getPalindromeString("madam"))


#prog for palindrome using slicing operator
def getPalindromeStringSlicing(str):
    return "palindrom string slicing" if str == str[::-1] else "not palindrome string slicing"

print(getPalindromeStringSlicing("madam"))


#prog for sum of its digits
def sumDigits(num):
    sum = 0
    
    while num > 0:
        digits = num % 10
        sum += digits
        num = num // 10
    return sum
print(sumDigits(123))

# prog to check prime no 
def is_prime(num):

    if num <= 1:
        return False

    for i in range(2, num):

        if num % i == 0:
            return False

    return True


print(is_prime(7))
print(is_prime(10))