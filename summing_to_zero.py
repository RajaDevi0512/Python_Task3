list_sum = [4,2,-3,1,6]
sub_string = []

n = len(list_sum)
value = 0

for i in range(n):
   current_sum = 0
   for j in range (i,n):
        current_sum += list_sum[j]
        # print(list_sum[j])
        if current_sum == value:
            sub_string = list_sum[i:j+1]
            print(sub_string)
       
if not sub_string:
    print("No sub string found")