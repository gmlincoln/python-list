#  Python List

Welcome to the **Python List Practice** guide!  
This file covers everything from basic to advanced list operations with examples and explanations.

---

## 📘 Table of Contents
1. [Create Lists](#create-lists)
2. [Access List Elements](#access-list-elements)
3. [Modify List Elements](#modify-list-elements)
4. [Add Elements](#add-elements)
5. [Remove Elements](#remove-elements)
6. [List Operations](#list-operations)
7. [Looping Through Lists](#looping-through-lists)
8. [List Comprehensions](#list-comprehensions)
9. [Sorting and Reversing](#sorting-and-reversing)
10. [Built-in Functions](#built-in-functions)
11. [Nested Lists](#nested-lists)
12. [Copying Lists](#copying-lists)
13. [Advanced Practice](#advanced-practice)
14. [Mini Projects](#mini-projects)

---

## 🧩 Create Lists

```python
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
mixed = [1, "hello", 3.14, True]
print(fruits)
```

```bash
Output:
['apple', 'banana', 'cherry']

```
🎯 Access List Elements

```python
fruits = ["apple", "banana", "cherry", "orange"]
print(fruits[0])     # First item
print(fruits[-1])    # Last item
print(fruits[2])     # Element at index 2
```
✏️ Modify List Elements

```python
fruits = ["apple", "banana", "cherry", "orange"]
fruits[1] = "grape"
print(fruits)

nums = [10, 20, 30, 40, 50]
nums[-2:] = [60, 70]
print(nums)
```
➕ Add Elements

```python
fruits.append("mango")
fruits.insert(1, "orange")
fruits.extend(["kiwi", "papaya"])
print(fruits)
```
➖ Remove Elements

```python
fruits.remove("banana")   # Remove by value
fruits.pop()              # Remove last item
del fruits[1]             # Remove by index
fruits.clear()            # Remove all
print(fruits)
```
🔁 List Operations

```python
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)       # Concatenate
print(a * 2)       # Repeat
print("apple" in ["apple", "banana"])
```
🔄 Looping Through Lists

```python
fruits = ["apple", "banana", "cherry"]

# Simple loop
for fruit in fruits:
    print(fruit)

# With index
for i, fruit in enumerate(fruits):
    print(i, fruit)
```
⚙️ List Comprehensions

```python

# Squares of numbers
squares = [x**2 for x in range(1, 6)]

# Filter even numbers
nums = [10, 25, 30, 45, 60]
evens = [n for n in nums if n % 2 == 0]
```
#### Uppercase conversion
```python 
fruits = ["apple", "banana", "cherry"]
upper = [f.upper() for f in fruits]
print(squares, evens, upper)
```
🧮 Sorting and Reversing

```python

numbers = [4, 1, 8, 3]
numbers.sort()
print(numbers)      # Ascending

numbers.sort(reverse=True)
print(numbers)      # Descending

numbers.reverse()
print(numbers)
```
📊 Built-in Functions

```python 

nums = [2, 8, 3, 7]
print(len(nums))   # 4
print(max(nums))   # 8
print(min(nums))   # 2
print(sum(nums))   # 20

fruits = ["apple", "banana", "apple"]
print(fruits.index("banana"))  # 1
print(fruits.count("apple"))   # 2 

```

🧱 Nested Lists

```python 
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][1])  # 5

# Print all elements
for row in matrix:
    for num in row:
        print(num, end=" ")
```
📋 Copying Lists
``` python

list1 = [1, 2, 3]
list2 = list1.copy()
list3 = list1[:]


list1.append(4)
print(list1)
print(list2)
```
⚡ Advanced Practice
```python

# Remove duplicates
nums = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(nums))

# Merge unique
a = [1, 2, 3]
b = [3, 4, 5]
merged = list(set(a + b))

# Intersection
common = list(set(a) & set(b))

# Flatten nested
nested = [[1, 2], [3, 4]]
flat = [x for sub in nested for x in sub]

print(unique, merged, common, flat)
```
### 💡 Mini Projects
🧮 1. Student Marks Analyzer
```python

marks = [85, 90, 78, 92, 88]
print("Average:", sum(marks)/len(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))
```
🛒 2. Shopping Cart
```python
cart = []
cart.append("Milk")
cart.append("Bread")
cart.remove("Milk")
print(cart)
```
📄 3. Unique Word Extractor

```python

text = "Python is fun and Python is powerful"
words = text.split()
unique_words = list(set(words))
print(unique_words)

```
🧠 Practice Task
At the end of this page, find the Practice Section and try solving the exercises by yourself!

🏁 Summary
Lists are one of Python’s most powerful and flexible data structures.
They allow you to store, modify, and iterate over collections of data easily.

Keep practicing the above examples and challenges to master lists in Python!




# 📘 Python Tuple

## 🧠 What is a Tuple?
A **tuple** in Python is a collection of items that is:

- **Ordered**
- **Immutable** (cannot be changed after creation)
- Allows **duplicate values**
- Can store **multiple data types**

Tuples are written using **parentheses `( )`**.

### Example
```python
my_tuple = (10, 20, 30)
print(my_tuple)
```

### ✨ Why Use Tuples?
- Faster than lists  
- Data remains safe because tuples cannot be changed  
- Can be used as dictionary keys  
- Good for fixed data  

### 📍 1. Creating Tuples
#### ✔ Normal Tuples
```python
numbers = (1, 2, 3, 4)
```

#### ✔ Tuple with multiple data types

```python
student = ("Rahim", 21, 3.75, True)
```

#### ✔ Tuple without parentheses (tuple packing)
```python
fruits = "apple", "mango", "banana"

```

#### ✔ Single-item Tuple (Important)
```python
single = (10,)       # Correct
not_tuple = (10)     # Wrong → This is an integer

```

### 📍 2. Accessing Tuple Items
#### ✔ Access by index
```python
numbers = (10, 20, 30, 40)
print(numbers[0])   # 10
print(numbers[2])   # 30

```
#### ✔ Negative indexing
```python
print(numbers[-1])  # 40
print(numbers[-2])  # 30

```


### 📍 3. Slicing Tuples
####
```python
letters = ('a', 'b', 'c', 'd', 'e')

print(letters[1:4])   # ('b', 'c', 'd')
print(letters[:3])    # ('a', 'b', 'c')
print(letters[2:])    # ('c', 'd', 'e')

``` 
### 📍 4. Looping Through Tuples
#### ✔ Using for loop
```python
colors = ("red", "green", "blue")

for c in colors:
    print(c)

```
#### ✔ Using index

```python
for i in range(len(colors)):
    print(colors[i])

```

### 📍 5. Useful Tuple Methods
#### ✔ count()
Counts how many times a value appears.

```python
numbers = (1, 2, 3, 2, 4, 2)
print(numbers.count(2))   # 3

```
#### ✔ index()
Returns the index of the first occurrence.

```python
print(numbers.index(3))   # 2

```
### 📍 6. Tuple Unpacking
#### ✔ Basic Unpacking
```python
person = ("Rafi", 25, "Dhaka")

name, age, city = person

print(name)  # Rafi
print(age)   # 25
print(city)  # Dhaka

```
#### ✔ Using * (Star) for multiple values
```python
values = (10, 20, 30, 40, 50)

a, b, *rest = values

print(a)     # 10
print(b)     # 20
print(rest)  # [30, 40, 50]

```



###  📍 7. Tuple vs List (Quick Comparison) 

| Feature    | Tuple      | List         |
| ---------- | ---------- | ------------ |
| Syntax     | `( )`      | `[ ]`        |
| Changeable | ❌ No       | ✅ Yes        |
| Faster     | ✅ Yes      | ❌ No         |
| Used For   | Fixed data | Dynamic data |

### 📍 8. Practical Examples
#### ✔ Example 1: Return multiple values from a function
```python 
def calculate(a, b):
    return (a + b, a * b)

sum_result, mul_result = calculate(10, 5)

print(sum_result)  # 15
print(mul_result)  # 50

```
#### ✔ Example 2: List of tuples (student records)
```python
 students = [
    ("Shuvo", 24),
    ("Fairoz", 23),
    ("Tamim", 22),
    ("Sayem", 25)
]

```

### 📍 9. Practice Questions
#### ✔ Basic
- Create a tuple with 5 items and print each item.  
- Create a tuple of numbers and find the sum.   
- Print the last item of a tuple using negative indexing.  

#### ✔ Intermediate
- Slice a tuple to get the middle three items.  
- Count how many times a value appears in a tuple.  
- Unpack a tuple into 4 variables.
  
#### ✔ Advanced
- Write a function that returns (min_value, max_value) without using min() or max().  
- Store multiple student records using a list of tuples and print only the names.  
- Modify the tuple value using index number [you can search it]


