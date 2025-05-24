decimalNumber=int(input("Enter a decimal number: "))
x=decimalNumber 
a = []
while x>0:
    a.append(x%2)
    x=x//2

a.reverse()
print("Binary value using python code: ",*a,sep='')

#easy way using ready method
print("Binary value using built in method: ", bin(decimalNumber))
