# Count how many digits in a number

n = 5873
count = 0

while n > 0:
    count += 1
  #this shi will count the digits until it appraches to zero lol
    n = n // 10

print(count)
