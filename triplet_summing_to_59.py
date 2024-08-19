list_sum = [10,20,30,9]
sub_string = []

n = len(list_sum)
value = 59

for i in range(n): # outerloop 
   current_sum = 0
   for j in range (i,n): 
        current_sum += list_sum[j]
        if current_sum == value:
            sub_string = list_sum[i:j+1]
            print(sub_string)
       
if not sub_string:
    print("No sub string found")
