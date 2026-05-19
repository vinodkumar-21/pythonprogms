"""
Returns values one by one using yield.

A generator is a special function that uses yield instead of return. 
It returns a generator object and produces values one at a time on demand. 
Generators are memory-efficient because they do not store all values in memory at once; 
execution pauses at each yield and resumes when the next value is requested.

Instead of loading the entire file into memory, the generator returns one line at a time, which is very memory efficient.
"""
def numbers():
    yield 1
    yield 2
    yield 3

# Create generator object
gen = numbers()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3


#for printing square no
def square_numbers(n):
    for i in range(1, n + 1):
        yield i * i

for square in square_numbers(5):
    print(square)