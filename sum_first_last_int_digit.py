# to sum first and last digit of an integer
num = 12345
stringconvert = str(num) # converting int to str

first_digit = int(stringconvert[0]) # accessing first digit and converting str to int
last_digit =  int(stringconvert[-1]) # accessing last digit and converting str to int

sum = first_digit + last_digit
print (sum)

    
