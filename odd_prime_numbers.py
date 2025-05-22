def is_prime(n):
    if n <= 1:
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

start= int(input("Enter the starting number: "))
end= int(input("Enter the ending number: "))

i=start
if i%2==0:
    i+=1
while i<=end:
    if is_prime(i):
        print(i, "is a odd prime number")
    i+=2
