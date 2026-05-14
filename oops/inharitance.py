#1. Single Inheritance
# One child inherits from one parent.

#Real-World Example
# Son inherits from Father.

class Father:
    def house(self):
        print("this is father's house")

class Child(Father):
    pass
    # super().house()   # call Father method
    # print("Son's House")

obj = Child()
obj.house()

    
# 2. Multiple Inheritance
# One child inherits from multiple parents.

# Real-World Example
# A child learns:
# cooking from mother
# business from father

class Father:

    def business(self):
        print("Business Skill")


class Mother:

    def cooking(self):
        print("Cooking Skill")


class Child(Father, Mother):
    print("this is child class")
    # pass


c = Child()

c.business()
c.cooking()



# 3. Multilevel Inheritance
# Inheritance chain.

# Real-World Example
# Grandfather → Father → Son

class GrandFather:

    def land(self):
        print("Land")


class Father(GrandFather):

    def house(self):
        print("House")


class Son(Father):
    pass


s = Son()

s.land()
s.house()


# 4. Hierarchical Inheritance
# Multiple children inherit from one parent.

# Real-World Example
# One teacher teaches many students.

class Parent:

    def property(self):
        print("Property")


class Son(Parent):
    pass


class Daughter(Parent):
    pass


s = Son()
d = Daughter()

s.property()
d.property()


# 5. Hybrid Inheritance
# Combination of multiple inheritance types.

# Real-World Example
# Company structure with managers, employees, departments.

class A:

    def show_a(self):
        print("Class A")


class B(A):

    def show_b(self):
        print("Class B")


class C(A):

    def show_c(self):
        print("Class C")


class D(B, C):
    pass


d = D()

d.show_a()
d.show_b()
d.show_c()