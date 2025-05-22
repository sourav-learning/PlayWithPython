number = int(input("Enter a number for which you want the table to be generated: "))
print("Here is the table of ", number)
print("========================")
for i in range(1,11):
    #loop through 1 to 10
    print(number, 'X', i, "=", number*i)