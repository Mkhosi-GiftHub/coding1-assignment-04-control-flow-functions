def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer: The loop goes through each number in [1, 2, 3].The if condition filters out numbers greater than 1, so only 2 and 3 are passed to add_one. Answer is 3 and 4

# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer:add_one(2) returns 3 because return sends a value back to the caller, while print only displays text and does not give the program a usable value.
