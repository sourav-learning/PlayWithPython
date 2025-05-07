a = 5
print("a is of type ", type(a))  # <class 'int'>
print("a is instance of int - ", isinstance(a, int))  # True

b = 5.0
print("b is of type ", type(b))  # <class 'float'>
print("b is instance of float - ", isinstance(b, float))  # True

c = a + b
print("c is of type ", type(c))  # <class 'float'>
print("c is instance of int - ", isinstance(c, int))  # False

listOfRollNos = [1, 5, 7, 2, 8, 3]
print("listOfRollNos is of type ", type(listOfRollNos))  # <class 'list'>
print("3rd roll no in the list is ", listOfRollNos[2]) 
print("sorted list of roll no is ", sorted(listOfRollNos))  # [1, 2, 3, 5, 7, 8]

name = "Sourav K Chatterjee"
print("name is of type ", type(name))  # <class 'str'>
print("Printing the name in reverse order ", name[::-1])  

print("Printing the name in title case : ", name.title())  # Sourav K Chatterjee

name = "     Taj Mahal     "
print("remove extra spaces from the left of the string :", name.lstrip(), "is locationed in Agra")  # Taj Mahal
print("remove extra spaces from the right of the string :", name.rstrip(), "is locationed in Agra")  #      Taj Mahal
print("remove extra spaces from the both side of the string :", name.strip(), "is locationed in Agra")  # Taj Mahal

#sort a list of names
listOfNames = ["Sourav", "Arnab", "Zoheb", "Amit", "Suman"]
listOfNames.sort()
print("listOfNames in alphabetical order ", listOfNames)  # ['Amit', 'Arnab', 'Sourav', 'Suman', 'Zoheb']
listOfNames.sort(reverse=True)
print("listOfNames in reverse alphabetical order ", listOfNames)  # ['Zoheb', 'Suman', 'Sourav', 'Arnab', 'Amit']
listOfNames.insert(2, "Satyajit")
print("listOfNames after inserting Satyajit at 2nd position ", listOfNames)  # ['Zoheb', 'Suman', 'Satyajit', 'Sourav', 'Arnab', 'Amit']    

listOfNames.remove("Arnab")
print("listOfNames after removing Arnab ", listOfNames)  # ['Zoheb', 'Suman', 'Satyajit', 'Sourav', 'Amit']

listOfNames.append("Joy")
listOfNames.sort()
print("listOfNames in alphabetical order after appending Joy ", listOfNames)  # ['Amit', 'Joy', 'Satyajit', 'Sourav', 'Suman', 'Zoheb']

print("Print twice :",listOfNames*2)  # ['Amit', 'Joy', 'Satyajit', 'Sourav', 'Suman', 'Zoheb', 'Amit', 'Joy', 'Satyajit', 'Sourav', 'Suman', 'Zoheb']

# Play with tuple
listOfRollNos = (1, 5, 7, 2, 8, 3)
print("listOfRollNos is of type ", type(listOfRollNos))  # <class 'tuple'>
print("3rd roll no in the list is ", listOfRollNos[2])
print("sorted list of roll no is ", sorted(listOfRollNos))  # [1, 2, 3, 5, 7, 8]
#listOfRollNos.sort(reverse=True)
# AttributeError: 'tuple' object has no attribute 'sort' However sorted method does not modify the 
# original tuple. It returns a new sorted list.

listOfCountries = ["India", "USA", "UK", "China", "Japan"]
print("listOfCountries: ", listOfCountries) # ['India', 'USA', 'UK', 'China', 'Japan']
listOfCountries.append("Nepal")  
print("listOfCountries after appending Nepal: ", listOfCountries) # ['India', 'USA', 'UK', 'China', 'Japan', 'Nepal']
listOfCountries.pop(2)
print("listOfCountries after removing 2nd element: ", listOfCountries) # ['India', 'USA', 'China', 'Japan', 'Nepal']
listOfCountries.insert(2, "Spain")
print("listOfCountries after inserting Spain at 2nd position: ", listOfCountries) # ['India', 'USA', 'Spain', 'China', 'Japan', 'Nepal']