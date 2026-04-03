# reverse_and_palindrome.py
"""
🔢 Reversing a Number & Palindrome Check

Logic:
- Extract last digit using % 10
- Remove last digit using // 10
- Build reversed number using rev = rev * 10 + digit

Time Complexity: O(log10(n))  -> number of digits
Space Complexity: O(1)        -> constant space
"""

def reverse_number(n):
    num = n
    rev = 0

    while num > 0:
        digit = num % 10
        rev = (rev * 10) + digit
        num = num // 10

    return rev


def is_palindrome(n):
    return n == reverse_number(n)


# 🔹 Main Execution
if __name__ == "__main__":
    n = int(input("Enter a number: "))

    reversed_num = reverse_number(n)
    print("Reversed number:", reversed_num)

    if is_palindrome(n):
        print("Palindrome: YES")
    else:
        print("Palindrome: NO")
