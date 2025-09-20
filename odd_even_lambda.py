isOdd = lambda n: n%2!= 0

n = int(input("Enter a number to check even or odd : "))
if(isOdd(n)):
    print("Odd number")
else:
    print("Even number")
