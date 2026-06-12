# List : mutable,hetrogeneous,ordered,allow duplicates
# List is a collection of items which are ordered and changeable. Allows duplicate members.
# List is defined by using square brackets [] and items are separated by commas.

# cresating empty list
my_list2 = list()
# print(my_list2)

# creating list and initializing
my_list = [1, 2, 3, "Hello", 3.14, True]

## Type of the list
print(type(my_list)) # <class 'list'>

# Accessing the elements in the list

## printing any one element inside the list
# print(my_list[0])
 
## printing by looping 
# for i in my_list:
#     print(i)
# i=0
# while(i<len(my_list)):
#     print(my_list[i])
#     i+=1

# Checking whether the element is present inside the list
# if 3.14 in my_list:
#     print("yes")
# if "banana" in my_list:
#     print("yes")
# else: 
#     print("no")
# print("yes") if 2 in my_list else print("no")

# Few operations in list 

## adding element at the last index 
fruit = list(["apple","banana"])
my_list.append(fruit)
# print(my_list)

## adding a element at the specific index
# my_list[6].insert(2,"lemon")
# print(my_list)

## removing the element from the last index
# my_list.pop()
# print(my_list)

## removing the element from the list if element known
# my_list[6].remove("banana")
# print(my_list)

## removing entire list
# my_list[6].clear()
# print(my_list)

## reversing a list
# my_list.reverse()
# my_list[0].reverse()
# print(my_list)

my_list3 = [6,4,5,18,25]
## Sorting in the list
# my_list3.sort()
# print(my_list3)
# my_list3.sort(reverse=True)
# print(my_list3)
# new_sorted_my_list3 = sorted(my_list3, reverse = True)
# print(new_sorted_my_list3)

## concatenating two lists and slicing
new_list = [1,2,3,4]
new_list2 = [5,6,7,8]
#  use "+"
# print(new_list + new_list2)
# print(new_list[:]) #[start:end:step] ## end is always not consider end-1
# print(new_list[1:4]) # [2,3,4]
# print(new_list[1:]) # [2,3,4]
# print(new_list[:4]) # [1,2,3,4]
# print(new_list[1:4:2]) # [2,4]
# print(new_list[::2]) # [1,3]
# print(new_list[::-1]) # [4,3,2,1]

## If i assign the org to cpy list the object is same 
list_org = [1,2,3,4]
# list_cpy = list_org # To avoid the object pointing 3 methods are there
# 1. using copy method
# list_cpy = list_org.copy()
# 2. using slicing
# list_cpy = list_org[:]
# 3. using the list() constructor
# list_cpy = list(list_org)
# list_cpy.append(5)
# print(list_org)
# print(list_cpy)

## list comprehension
# squares = [x**2 for x in list_org[::-1]]
# print(list_org)
# print(squares)