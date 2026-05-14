# Different classes have the same method name, but each behaves differently.

# Real-world Example
# Think about a payment system.
# Different payment methods have the same action → pay()
# But behavior is different.

# Different behavior depending on object.

# That is Polymorphism.

# Another real-world examples:

# start() → Car, Bike, Bus
# login() → Admin, User, Guest
# notification() → Email, SMS, Push Notification

#method overloading is not supported in python 
# if you want then use keargs



class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


d = Dog()
c = Cat()

d.sound()
c.sound()



# Real-world Example
# Think about a payment system.
# Different payment methods have the same action → pay()
# But behavior is different.

class CreditCard:

    def pay(self):
        print("Paid using Credit Card")


class UPI:

    def pay(self):
        print("Paid using UPI")


class Cash:

    def pay(self):
        print("Paid using Cash")


payments = [CreditCard(), UPI(), Cash()]

for p in payments:
    p.pay()