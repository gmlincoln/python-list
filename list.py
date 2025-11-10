
# list_name = [item1, item2, item3.....itemN]


# fruits = ["apple", "banana", "cherry"]

numbers = [10, 20, 30, 40, 50]

mixed = [1, "hello", 3.14, True]

#Access List Elements
# find item no 2 from fruits list

# print(fruits[1])

# # find item 5 from numbers list
# print(numbers[4])
# #mixed -3
# print(mixed[-3])


#Modify List Elements
#fruits = ["apple", "banana", "cherry"]

# print(fruits)

# fruits[1] = "mango"

# print(fruits)

# fruits[-1] = "licchi"

# print(fruits)

# nums = [10, 20, 30, 40, 50]

# # print(nums[-2:])


# nums[-2:] = [60, 70]
# # print(nums)

# #[10, 20, 30, 60, 70]
# nums[1:3] = [15, 25]

# # print(nums)
# #[10, 15, 25, 60, 70]


fruits = ["apple", "banana", "cherry"]

fruits.append("mango")

# print(fruits)
#["apple", "banana", "cherry", "mango"]
fruits.insert(2, "licchi")

# print(fruits)

fruits_two = ["blueberry", "orange"]

fruits.extend(fruits_two)

# print(fruits)

#['apple', 'banana', 'licchi', 'cherry', 'mango', 'blueberry', 'orange']

# fruits.remove("banana")   # Remove by value
# print(fruits)

# fruits.clear()

# print(fruits)

# del fruits[1]             

# print(fruits)

# fruits.pop()


# print(fruits)

# nums1 = [4, 1, 8, 3]
nums2 = [5, 6, 7, 4]

# print(nums1.extend(nums2))
# print(nums1+nums2)

# print(nums1 * 2) # [4, 1, 8, 3, 4, 1, 8, 3]


# nums1.sort()
# print(nums1)   

# nums1.sort(reverse=True)
# print(nums1)





# numbers.sort(reverse=True)
# print(numbers)      # Descending
nums1 = [4, 1, 8, 3]

# nums1.sort(reverse=True)
nums1.reverse()
print(nums1)

# nums1.reverse()
# print(nums1)


# nums1 = [4, 1, 8, 3]


# for i in range(0, len(nums1), 1):
#     print(nums1[i]*2)



####### Make a cart list
### add item in this cart 
### and print your cart


