"""
basics things to write a program

suit - A suite is simply a block of code that belongs together, usually under statements like:

if
for
while
def
class

👉 In most languages, blocks use { }
👉 In Python, a suite is defined by indentation
A suite = block of code
Defined using indentation
Used in loops, conditions, functions, classes


slice operator - The slice operator in Python lets you extract parts of a sequence (like a string, list, or tuple) using a compact syntax.

data types in python - In Python, data types define the kind of value a variable holds and what operations you can perform on it. Python is dynamically typed, so you don’t declare types explicitly.
1. Numeric Types
x = 10        # int
y = 3.14      # float
z = 2 + 3j    # complex
int → whole numbers
float → decimal numbers
complex → real + imaginary (a + bj)

2. String (str)
name = "Vinod"
Sequence of characters
Immutable (cannot change directly)

3. List (Mutable)
nums = [1, 2, 3, 4]
Ordered, changeable (mutable)
Allows duplicate values

4. Tuple (Immutable)
t = (1, 2, 3)
Ordered, not changeable
Faster than lists

5. Dictionary (dict)
student = {"name": "Vinod", "age": 22}
Key-value pairs
Keys must be unique

6. Set
s = {1, 2, 3}
Unordered
No duplicates allowed

7. Boolean (bool)
is_active = True
Only two values: True, False
Used in conditions

8. NoneType
x = None
Represents no value / null

Mutable vs Immutable (Important for interviews)
👉 Immutable
int, float, str, tuple
Cannot change after creation
👉 Mutable
list, dict, set
Can modify values

Quick Summary Table
Type	Example	Mutable
int	10	❌
float	3.14	❌
str	"hello"	❌
list	[1,2,3]	✅
tuple	(1,2,3)	❌
dict	{"a":1}	✅
set	{1,2,3}	✅
bool	True	❌
NoneType	None	❌

👉 id() shows object identity (memory reference), and
👉 "H" + s[1:] creates a new string, not modifying the original.


different types of functions - 
1. Built-in Functions

Provided by Python itself.

print(len("hello"))   # 5
print(type(10))       # <class 'int'>

✔️ No need to define them

🧩 2. User-defined Functions

Functions you create using def.

def add(a, b):
    return a + b

print(add(2, 3))
⚡ 3. Lambda Functions (Anonymous Functions)

Small one-line functions without a name.

square = lambda x: x * x
print(square(5))

✔️ Used in map(), filter(), sorting, etc.

🔄 4. Recursive Functions

Function calls itself.

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))
📦 5. Functions with Default Arguments
def greet(name="Guest"):
    return "Hello " + name

print(greet())
🔑 6. Keyword Argument Functions
def info(name, age):
    print(name, age)

info(age=22, name="Vinod")
🔢 7. Variable-length Arguments
👉 *args (tuple)
def add(*nums):
    return sum(nums)

print(add(1,2,3,4))
👉 **kwargs (dictionary)
def details(**data):
    print(data)

details(name="Vinod", age=22)
🔁 8. Higher-Order Functions

Functions that take another function as argument or return one.

def apply(func, value):
    return func(value)

print(apply(lambda x: x*2, 5))
🧱 9. Nested Functions

Function inside another function.

def outer():
    def inner():
        print("Inner")
    inner()

outer()
🧠 10. Generator Functions

Use yield instead of return.

def count_up(n):
    for i in range(n):
        yield i

for num in count_up(3):
    print(num)

✔️ Memory efficient

🔒 11. Decorator Functions

Used to modify behavior of other functions.

def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()
⚡ Quick Summary
Type	Use Case
Built-in	Predefined utilities
User-defined	Custom logic
Lambda	Short one-liners
Recursive	Problems like factorial
Default args	Optional parameters
*args/**kwargs	Flexible inputs
Higher-order	Functional programming
Generator	Large data / streams
Decorator	Modify behavior

🚀 Interview Insight
Most asked: **lambda, recursion, decorators, *args/kwargs
Generators are important for performance optimization


⚡ Key Understanding
Function	Purpose
map()	Transform each element
filter()	Select elements based on condition
sorted() + lambda	Custom sorting logic


json.loads
json.load



🔹 Relationship
You use FastAPI to build REST APIs
REST = “what rules to follow”
FastAPI = “tool to implement those rules”
🔹 Quick Analogy
REST API = traffic rules 🚦
FastAPI = the car 🚗 you use to drive following those rules


class and object example
we have class and variable name and age how to print these variable
init method - it is a constructor in python
self keyword
pass - it is the keyword which is used insted of statement like to show blank statement we need to pass in any conditions
regx - regex



What is a decorator in Python?
✅ Answer
A decorator is a function that wraps another function to extend its behavior without modifying its code. It is commonly used for logging, authentication, and validation.
👉 Bonus:
In Django, decorators like login_required are built-in, while in Flask we often create custom decorators.


patch and put


s = "hello world python"
arr = s.split()

print(arr)


decorator - it is used to modify and extend the behaviour of a function without changing the actual code
🔧 Core Idea

Instead of editing a function directly, you wrap it inside another function.

📌 Basic Syntax
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

Usage:

@my_decorator
def say_hello():
    print("Hello")

say_hello()
Output:
Before function runs
Hello
After function runs


error handling - Error handling in Python is about detecting, managing, and recovering from runtime exceptions so your application doesn’t crash unpredictably.
🔧 1. Basic Syntax (try–except)
try:
    x = int("abc")   # error
except ValueError:
    print("Conversion failed")

🎯 2. Multiple Exceptions    
try:
    x = int("10")
    y = 10 / 0
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Division by zero")

multi threading and multi processing - Both multithreading and multiprocessing are concurrency techniques, but they solve different classes of performance problems. Given your backend work (Flask/Django + queues), understanding the distinction is critical.
Multithreading → lightweight, I/O tasks
Multiprocessing → heavy CPU tasks

gil - global interpreter lock


string to list => split
list to string => join

| Operation          | Method                 |
| ------------------ | ---------------------- |
| List → String      | `"sep".join(list)`     |
| String → List      | `str.split(sep)`       |
| List(int) → String | `join(map(str, list))` |
| String → List(int) | `map(int, split())`    |


mro
101001010 prog
hacker rank prog
mysql
aws
gen ai
decorator
event loop
asgi and wsgi
uvicorn
reverse proxy
nginx

how to upload large mb file like 5 gb 10 gb and 20 gb
upload 5 lak data

sanack ladder game 

threading helps mainly with I/O-bound tasks, not CPU-heavy computation.


Mutable vs Immutable
Mutable

Can change after creation:

list
dict
set

Example:

a = [1,2]
a.append(3)
Immutable

Cannot change after creation:

tuple
str
int
float

Example:

x = "abc"
x = x + "d"

(New object created internally)


Memoization


self refers to the current object of the class.
middleware in python
solid principal
design pattern
gil -> global interpreter lock
MRO (Method Resolution Order).
24. What is Depends() in FastAPI?
23. What is Dependency Injection in FastAPI?
iter and generator (yeild)
36. What is Connection Pooling?


37. What is SOLID Principle?
Answer

Five OOP design principles:

S → Single Responsibility
O → Open/Closed
L → Liskov Substitution
I → Interface Segregation
D → Dependency Inversion

Real-world Meaning of SOLID
Principle	Meaning
SRP	One class → One job
OCP	Extend code without modifying
LSP	Child should behave like parent
ISP	Don't force unnecessary methods
DIP	Depend on abstraction, not concrete class



Design Patterns

These are ready-made solutions for common software problems.

They tell:

how to solve specific design issues
reusable architecture ideas

Examples:

Singleton Pattern
Factory Pattern
Observer Pattern
MVC Pattern

Design Pattern answers:
👉 “What solution should I use for this problem?”


Quick Revision Table
Pattern	Purpose	Real-world Use
Singleton	One object only	DB Connection
Factory	Object creation	Payment/Vehicle creation
Observer	Notify multiple objects	Notifications
MVC	Separate logic/UI/data	Django/Laravel

merge 2 dict which have unique and both might have same key value


Most Asked FastAPI Questions (2–5 Years)
	Why FastAPI is faster?
	Sync vs Async?
	Dependency Injection?
	JWT authentication flow?
	SQLAlchemy session management?
	Middleware?
	Background tasks?
	Connection pooling?
	Pydantic validation?
	API versioning?
	
Most Asked Django Questions
	MVT architecture
	Middleware
	ORM
	Signals
	Authentication
	DRF serializers
	Query optimization
	select_related vs prefetch_related
Most Asked Flask Questions
	Blueprint
	Flask extensions
	Application context
	Request context
	Jinja2
	Session management


"""