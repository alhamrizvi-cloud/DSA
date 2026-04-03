x = 5873

while x > 0:
  last_digit = x % 10
  #which will give us input 3
  x = x // 10
  # which will return 5873 to 587 to 58..
  total += last_digit
return total
print(sum_of_digits(5873))  # Output: 23
  
