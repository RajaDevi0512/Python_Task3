#separate the list into even list and odd list
mylist = [10,501,22,37,100,999,87,351]
evenlist = []
oddlist = []

for num in mylist:
    
    if num % 2 == 0:
        evenlist.append (num)
    else:
        oddlist.append(num)
print("Evenlist", evenlist)
print ("OddList", oddlist)