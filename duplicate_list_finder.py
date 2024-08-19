#to find the duplicate vale in the given set of lists
list1 = [1,3,5,7,9]
list2 = [2,4,5,6,8]
list3 = [2,3,5,7]
duplicatelist = []

for num in list1: 
    if num in list2: # compare elemnets between list1 and list2
        for num in list3: # compare elemnets between list2 and list3
           duplicatelist.append(num) #Finally append it into a duplicatelist
print(duplicatelist)