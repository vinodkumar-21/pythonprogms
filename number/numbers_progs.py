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

