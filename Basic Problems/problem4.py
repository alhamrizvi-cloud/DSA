# Check Armstrong Number

n = 153
num = n
k = len(str(n))   # number of digits
total = 0

while num > 0:
    digit = num % 10
    total += digit ** k
    num = num // 10

if total == n:
    print("Armstrong Number")
else:
    print("Not Armstrong")
