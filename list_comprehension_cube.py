# User will input a range. We will find the prime numbers in the range and then output the cube of them
def onlyPrime(fun):
    def inner(fun):
        for num in range(start, end+1):
            if num <= 1:
                continue
            if(num == 2):
                primeNums.append(num)
                continue
            for i in range(2, num):
                if num%i == 0:
                    break
                if i == num-1:
                    primeNums.append(num)
        return inner
    return onlyPrime

@onlyPrime
def primeCube():
    start = int(input("Enter an integer to start the range : "))
    end = int(input("Enter an integer to end the range : "))
    #validation if the start is less than end
    if(start >= end):
        print("Error : The starting number should be less than the ending number")
outputLst = [] #output values to be stored
primeNums = []




        
print("Prime numbers", primeNums)   
outputLst = [x**3 for x in primeNums]         
print(outputLst)