# PlayWithPython
Basic python programs with various datatypes and functions

# Reverse the content of a list and print without comma
lst.reverse()
print(*lst, sep='')

# Tuples
* Tuples are immutable. You cannot assign. This is the difference between list and tuple
* If a tuple contains, single element then end it with comma.
* All functions that do not modify a tuple like length, max, min can be used
* [] is used for list whereas () is used for tuples

# Set 
* Initialized with {} 
* Set does not allow duplicates
* Set does not guarantee order. 
* Operations like a[1] is not allowed as the indexing is not supported
* a*3 is not allowed as set does not allow repetation.

* listOfRollNos.sort(reverse=True)
* AttributeError: 'tuple' object has no attribute 'sort' However sorted method does not modify the 
* original tuple. It returns a new sorted list.