#1. If the input is divisible by 3, the function will return the string "fizz"
#2. If the input is divisible by 5 it will return "Buzz"
#3. If the input is divisible by both 3 and 5 it will return "FizzBuzz"
#4. For any other number it will return the same input
def fizz_Buzz(input)
  if input % 3 == 0:
    return "fizz"
  if input % 5 == 0:
    return "buzz"
  if input % 3 == 0 and input % 5 == 0
    return "fizz buzz"
  return input

print(fizz_buzz(3))
