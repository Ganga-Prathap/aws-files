

Store

Let’s say, you have built a store that is filled with different grocery items. You have observed that customers are facing difficulty to find an item. So you have decided to write a program that would make it easy for users to search for items.

AssignmentID -OOP004

Submission Guidelines

Create a folder /home/ec2-user/environment/oop_submissions/{AssignmentID}. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/oop_submissions/OOP004/
Copy your code file to the submission folder. Make use of the below example command
$ cp car.py /home/ec2-user/environment/oop_submissions/OOP004
Coding Guidelines:

Write all your code in store.py file
Write the following classes to complete the assignment:

Item

An item has the following properties

name: Name of the item
price: Price of the item > 0
category: Category to which the item belongs to (any string value)
Coding Guidelines:

Write Item class in store.py file. It should behave as shown below.
>>> item = Item(name="Oreo Biscuits", price=30, category="Food")  
>>> print(item)  
Oreo Biscuits@30-Food  
>>> item = Item(name="Oreo Biscuits", price=0, category="Food")  
ValueError: Invalid value for price, got 0  
Query

A query is a request from the customer to the store. It has the following properties

field: Properties of Item on which customer is searching . In our case name or price or category
value: Value to which the item property is to be matched with
operation: Operations mentioned below
Coding Guidelines:

Write Query class in store.py file. It should behave as shown below.
>>> query = Query(field="name", operation="EQ", value="Oreo Biscuits")  
>>> print(query)  
name EQ Oreo Biscuits  
Store

A store is a collection of items. Customers can search for relevant items in the store. It should support the following functionality.

Add item:

Adds a new item to the store

>>> store = Store()  
>>> item = Item(name="Oreo Biscuits", price=30, category="Food")  
>>> store.add_item(item)  
Display all items:

Displays all the items in the store

>>> store = Store()  
>>> item = Item(name="Oreo Biscuits", price=30, category="Food")  
>>> store.add_item(item)  
>>> item = Item(name="Boost Biscuits", price=20, category="Food")  
>>> store.add_item(item)  
>>> print(store)  
Oreo Biscuits@30-Food  
Boost Biscuits@20-Food
Filter:

A filter method should filter the items in a store based on users preference (a Query object) and returns a Store object containing the filtered results.

Customers provide thier preference as Query object which represents their needs.

You code should be have as below.

>>> store = Store()  
>>> item1 = Item(name="Oreo Biscuits", price=30, category="Food")  
>>> store.add_item(item)  
>>> item2 = Item(name="Boost Biscuits", price=20, category="Food")  
>>> store.add_item(item)  
>>> item3 = Item(name="Butter", price=10, category="Grocery")  
>>> store.add_item(item)  
>>> query = Query(field="category", operation="IN", value=["Food"])  
>>> results = store.filter(query)  
>>> print(results)  
Oreo Biscuits@30-Food  
Boost Biscuits@20-Food  
Equals condition:
   >>> query = Query(field="name", operation="EQ", value="Oreo Biscuits")  
   >>> results = store.filter(query)  
   >>> print(results)  
   Oreo Biscuits@30-Food  
Explanation:

Query(field="name", operation="EQ", value="Oreo Biscuits")
Should filter all the items which have "Oreo Biscuits" as value for the field "name"

Greater Than condition:
>>> query = Query(field="price", operation="GT", value=20)  
>>> results = store.filter(query) 
>>> print(results)  
Oreo Biscuits@30-Food  
Explanation:

Query(field="price", operation="GT", value=20)
Should filter all the items which have value greater than 20 for the field "price"

Greater Than or Equal condition: "GTE"
>>> query = Query(field="price", operation="GTE", value=20)  
    >>> results = store.filter(query) 
    >>> print(results)  
    Oreo Biscuits@30-Food  
    Boost Biscuits@20-Food 
Explanation:

Query(field="price", operation="GTE", value=20)
Should filter all the items which have value greater than or equal to 20 for the field "price"

Less Than: "LT"
>>> query = Query(field="price", operation="LT", value=20)  
>>> results = store.filter(query) 
>>> print(results)  
Butter@10-Grocery
Explanation:

Query(field="price", operation="LT", value=20)
Should filter all the items which have value less than 20 for the field "price"

Less Than or Equal : "LTE"
>>> query = Query(field="price", operation="LTE", value=20)  
>>> results = store.filter(query) 
>>> print(results)  
Boost Biscuits@20-Food
Butter@10-Grocery
Explanation:

Query(field="price", operation="LTE", value=20)
Should filter all the items which have value less than or equal to 20 for the field "price"

StartsWith: "STARTS_WITH"
 >>> query = Query(field="name", operation="STARTS_WITH", value="Bu")  
>>> results = store.filter(query) 
>>> print(results)  
Butter@10-Grocery
Explanation:

Query(field="name", operation="STARTS_WITH", value="bu")
Should filter all the items which have value that starts with "bu" for the field "name"

EndsWith: "ENDS_WITH" - is used to as condition in Query object to filter items with field value that ends with the query value
>>> query = Query(field="name", operation="ENDS_WITH", value="cuits")  
>>> results = store.filter(query) 
>>> print(results)  
Oreo Biscuits@30-Food  
Boost Biscuits@20-Food 
Explanation:

Query(field="name", operation="ENDS_WITH", value="cuits")
Should filter all the items which have value that ends with "cuits" for the field "name"

Contains: "CONTAINS"
>>> query = Query(field="name", operation="CONTAINS", value="uit")  
>>> results = store.filter(query) 
>>> print(results)  
Oreo Biscuits@30-Food  
Boost Biscuits@20-Food
Explanation:

Query(field="name", operation="CONTAINS", value="cuits")
Should filter all the items which have value that contains "cuits" for the field "name"

Filter should return a new store object which has only the selected items.
>>> query = Query(field="price", operation="GT", value=15)  
>>> results = store.filter(query) # filter all items whose price is greater than 15 
>>> type(results)  # this is to show that results is another store object
<class '__main__.Store'>
>>> print(results)  
Oreo Biscuits@30-Food  
Boost Biscuits@20-Food  
Incase of empty results. Store should be have as below.
>>> query = Query(field="name", operation="STARTS_WITH", value="bu")  
>>> results = store.filter(query) 
>>> print(results)
No items
Exclude:

exclude is very similar to filter but works in an opposite way.
Similar to filter, It takes Query as a parameter
It returns a new Store object that contains all the items in the store except the ones which match the query.
>>> store = Store()  
>>> item = Item(name="Oreo Biscuits", price=30, category="Food")  
>>> store.add_item(item)  
>>> item2 = Item(name="Boost Biscuits", price=20, category="Food")  
>>> store.add_item(item)  
>>> item3 = Item(name="ParleG Biscuits", price=10, category="Food")  
>>> store.add_item(item)  
>>> print(store)  
Oreo Biscuits@30-Food  
Boost Biscuits@20-Food  
ParleG Biscuits@10-Food  
>>> query = Query(field="price", operation="GT", value=15)  
>>> results = store.exclude(query)  # exclude all items whose price is greater than 15 
>>> print(results)  
ParleG Biscuits@10-Food  
Exclude should return a new store object which has all the items that doesn’t match the query.
>>> query = Query(field="price", operation="GT", value=15)  
>>> results = store.filter(query) # filter all items whose price is greater than 15 
>>> type(results)  # this is to show that results is another store object
<class '__main__.Store'>
>>> print(results)  
ParleG Biscuits@10-Food
Chaining:

Queries can be chained i.e users should be able to perform further queries on the result of a query.

Hint: filter and exclude methods should return a new store object with filtered items.

>>> store = Store()  
>>> item = Item(name="Oreo Biscuits", price=30, category="Food")  
>>> store.add_item(item)  
>>> item = Item(name="Boost Biscuits", price=20, category="Food")  
>>> store.add_item(item)  
>>> item = Item(name="ParleG Biscuits", price=10, category="Food")  
>>> store.add_item(item)  
>>> query = Query(field="price", operation="GT", value=15)  
>>> results = store.filter(query)  
>>> print(results)  
Oreo Biscuits@30-Food  
Boost Biscuits@20-Food  
>>> new_query =  Query(field="name", operation="CONTAINS", value='Boost')  
>>> updated_results = results.exclude(new_query)  
>>> print(updated_results)  
Oreo Biscuits@30-Food  


Count:

Count of items in the store

>>> store = Store()  
>>> item = Item(name="Oreo Biscuits", price=30, category="Food")  
>>> store.add_item(item)  
>>> item = Item(name="Boost Biscuits", price=20, category="Food")  
>>> store.add_item(item)  
>>> item = Item(name="ParleG Biscuits", price=10, category="Food")  
>>> store.add_item(item)  
>>> store.count()  
3
Query

Should allow only the following operations.
IN
EQ
GT
GTE
LT
LTE
STARTS_WITH
ENDS_WITH
CONTAINS
Should raise a ValueError incase of invalid input.
>>> query = Query(field="name", operation="random", value="Oreo Biscuits")  
ValueError: Invalid value for operation, got random  
Back

















"""class Rectangle:
    
   def __init__(self, length, breadth):   
       self.length=length
       self.breadth=breadth
   
   def calculate_area(self):
       return self.length * self.breadth
       
   def calculate_perimeter(self):
       return (self.length+self.breadth)*2
       #return peri*2
     cde fg
m

e__ == "__main__":  
   rectangle_one = Rectangle(5, 5) 
   print("area of rectangle is ", rectangle_one.calculate_area()) 
   print("perimeter of rectangle is ",  rectangle_one.calculate_perimeter()) """