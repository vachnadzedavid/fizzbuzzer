#Counters of Fizz, Buzz, FizzBuzz and others are located in here :)
fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0
other_count = 0

#So basically what we do here is a loop through numbers from 1 to 100
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        fizzbuzz_count += 1
    elif i % 3 == 0:
        print("Fizz")
        fizz_count += 1
    elif i % 5 == 0:
        print("Buzz")
        buzz_count += 1
    else:
        print(i)
        other_count += 1

#Print the summary of counts after the loop finishes
print("Summary:")
print(f"Fizz: {fizz_count} times")
print(f"Buzz: {buzz_count} times")
print(f"FizzBuzz: {fizzbuzz_count} times")
print(f"Other numbers: {other_count} times")
