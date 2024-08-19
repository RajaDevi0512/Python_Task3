#sorting the list using bubble sort
list1 = [45,45,30,39,30,42,60,20,67,19,6]
# print(sorted(list1)) # simple way to sort in python
n = len(list1)
# print (n)
for i in range(n):
    # print (i)

# BUBBLE SORT
# I ==>range(0,11-0-1) that is range(0,10),
# II==> RANGE(0,9)
# III==> RANGE(0,7) and so on

    for j in range(0, n-i-1): 
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1],list1[j]
print(list1)


    