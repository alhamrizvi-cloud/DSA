def print_factors(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0:       # check if i is a factor
            result.append(i)   # add to the result list
    return result

# Example
num = 20
print(print_factors(num))  # Output: [1, 2, 4, 5, 10, 20]
