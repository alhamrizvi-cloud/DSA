x = 5873
total = 0

while x > 0:
    last_digit = x % 10
    total += last_digit
    x = x // 10

print(total)  # ✅ Output: 23
  
