# Return the product of digits
n = 234
num = n
total = 1
while num > 0:
    last_digit = num % 10
    total *= last_digit
    num = num // 10 
print(total)
