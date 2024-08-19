#To find the prime number in the given list
mylist = [10, 501, 22, 37, 100, 999, 87, 351]
# mylist = [1,2,4,5,6,7,19,37,47,351]
primenumberlist = []

def prime_check(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True # if not return true, we will not get any other prime number other than 2

for num in mylist:
    if prime_check(num):
        primenumberlist.append(num)

print("Prime numbers in the list:", primenumberlist)