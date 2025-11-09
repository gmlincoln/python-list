# 🐍 Python List Practice & Documentation

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
Output:

css
Copy code
['apple', 'banana', 'cherry']
🎯 Access List Elements
python
Copy code
fruits = ["apple", "banana", "cherry", "orange"]
print(fruits[0])     # First item
print(fruits[-1])    # Last item
print(fruits[2])     # Element at index 2
✏️ Modify List Elements
python
Copy code
fruits[1] = "grape"
print(fruits)

nums = [10, 20, 30, 40, 50]
nums[-2:] = [60, 70]
print(nums)
➕ Add Elements
python
Copy code
fruits.append("mango")
fruits.insert(1, "orange")
fruits.extend(["kiwi", "papaya"])
print(fruits)
➖ Remove Elements
```python
Copy code
fruits.remove("banana")   # Remove by value
fruits.pop()              # Remove last item
del fruits[1]             # Remove by index
fruits.clear()            # Remove all
print(fruits)
```
🔁 List Operations
```python
Copy code
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
#### ⚙️ List Comprehensions

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

``` python

list1 = [1, 2, 3]
list2 = list1.copy()
list3 = list1[:]

```
list1.append(4)
print(list1)
print(list2)
⚡ Advanced Practice
python
Copy code
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
💡 Mini Projects
🧮 1. Student Marks Analyzer
python
Copy code
marks = [85, 90, 78, 92, 88]
print("Average:", sum(marks)/len(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))
🛒 2. Shopping Cart
python
Copy code
cart = []
cart.append("Milk")
cart.append("Bread")
cart.remove("Milk")
print(cart)
📄 3. Unique Word Extractor
python
Copy code
text = "Python is fun and Python is powerful"
words = text.split()
unique_words = list(set(words))
print(unique_words)
🧠 Practice Task
At the end of this page, find the Practice Section and try solving the exercises by yourself!

🏁 Summary
Lists are one of Python’s most powerful and flexible data structures.
They allow you to store, modify, and iterate over collections of data easily.

Keep practicing the above examples and challenges to master lists in Python!

✍️ Author: Golam Maula Lincoln
🎓 Topic: Python List Practice
📅 Updated: November 2025