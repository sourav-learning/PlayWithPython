listOfNumber = eval(input("Enter a list of integers : "))
print(listOfNumber)
uniqueList = []
for each_number in listOfNumber:
    if each_number not in uniqueList:
        uniqueList.append(each_number)
print("Unique list using logic")
print(uniqueList)
s1 = set(listOfNumber)
print("Unique list using set")
print(s1)