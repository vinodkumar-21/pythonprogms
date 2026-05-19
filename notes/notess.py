"""Similarity with PHP
| Python | PHP Equivalent       |
| ------ | -------------------- |
| List   | Indexed Array        |
| Tuple  | Fixed Array (almost) |
| Set    | array_unique concept |
| Dict   | Associative Array    |

Mutable vs Immutable in Python
Mutable

A mutable object means:
👉 Value can be changed after creation

Examples:

List
Dictionary
Set
Immutable

An immutable object means:
👉 Value cannot be changed after creation

Examples:

String
Tuple
Integer
Float

MRO => Method Resolution Order
MRO (Method Resolution Order) is the order in which Python searches for a method or attribute in a class hierarchy, especially when multiple inheritance is used.
MRO (Method Resolution Order) is the order in which Python searches for methods and attributes in a class hierarchy. It is especially important in multiple inheritance. 
Python uses the C3 Linearization algorithm to determine the lookup order. We can view the MRO using ClassName.mro() or ClassName.__mro__.


What is Middleware?
Middleware processes request and response.
Examples:
Authentication
Logging
Session management


Django Decorators
@login_required
@permission_required
@csrf_exempt



select_related() and prefetch_related() are used to optimize database access and avoid the N+1 query problem. 
select_related() works with ForeignKey and OneToOne relationships by performing an SQL JOIN and fetching related data in a single query. 
prefetch_related() works with ManyToMany and reverse ForeignKey relationships by executing separate queries and combining the results in Python, 
reducing the total number of database queries and improving performance.




"""
