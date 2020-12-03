# A list is a collection of multiple elements in python
myList1 = ['A string',67,False,8.9]
myList2 = [4,55,6,2]

# You can print the lists as well
print("myList1 = " + str(myList1))
print("myList2 = " + str(myList2))

# In lists, order matters, any element can be grabbed by its 'index'
# Index of an element starts from 0 and increases by one by each successive element
# Example, for the first list named "myList1" the elements have the following indices:

'''
Indices for myList1

Index	Value
0		'A string'
1		67
2		False
3		8.9
'''

'''
Indices for myList2

Index	Value
0		'A string'
1		67
2		False
3		8.9
'''

print()
# We can get specific value of element using an index, we can do this using '[]' like below
# print(myList1[0]) # OUTPUT = A string

# What will be the output of the below code snippet?, (myList1 = ['A string', 67, False, 8.9])
# print(myList1[2]) # OUTPUT = ?


'''
Some list operations
'''

# We can get the length of the list using 'len()' function
# length_of_list = len(myList2)
# print("Length of myList2 is "+str(length_of_list))

# We can add an element to the end by '.append()' method
# print("myList1 before adding element: "+str(myList1))
# myList1.append("Kabir")
# print("myList2 after adding an element: "+str(myList1))

print()
# We can remove an element at a specific index using ".pop()" method
# print("myList1 before deleting an element: "+str(myList1))
# myList1.pop(3) # We are removing element on index 3 OR removing 4th element which is '8.9'
# print("myList1 after deleting an element: "+str(myList1))

'''
**INTERMEDIATE ONLY**
'''

# We can also have multiple values printed out at once using 'splicing'
# You have to specify start
# print(myList1[1:3]) # Will print elements starting from index one upto index 3(not including three)