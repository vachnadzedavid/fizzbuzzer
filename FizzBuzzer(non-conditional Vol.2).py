def fizz_Buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "fizz buzz"
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return "buzz"
    return input

# Test cases
print(fizz_Buzz(3))   # Output: "fizz"
print(fizz_Buzz(5))   # Output: "buzz"
print(fizz_Buzz(15))  # Output: "fizz buzz"
print(fizz_Buzz(7))   # Output: 7
