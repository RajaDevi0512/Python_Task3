# To print the first non-repeating value

#list1 = [1,1,2,2,3,3,3,5,6,6,7,8,9,12]
# list1= [2,3,3,4,5,6,6,7,9]
list1= [45,45,30,39,30,42,60]
non_repeating_list = []

for num in list1: 
    # print(num)
    if(list1.count(num)) == 1:
        non_repeating_list.append(num)
print(non_repeating_list[0])

