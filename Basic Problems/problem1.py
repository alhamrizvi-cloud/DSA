# Write a program to extract and print all digits of a number using a loop.

n = 5873

while n > 0:
    digit = n % 10   # get last digit
    print(digit) 
    n = n // 10      # remove last digit from number

# Output:
# 3
# 7
# 8
# 5
