# FizzBuzz problem using for loop
for i in range(1, 101):
    if (i%3==0 and i%5==0):
        print("FizzBuzz")
    elif (i%3==0):
        print("Fizz")
    elif (i%5==0):
        print("Buzz")
    else:
        print(i)

print("---------------")

#FizzBuzz problem uisng while loop
count = 1
while count <= 100:
    if (count % 3 == 0 and count % 5 == 0):
        print("FizzBuzz")
    elif (count % 3 == 0):
        print("Fizz")
    elif (count % 5 == 0):
        print("Buzz")
    else:
        print(count)
    count += 1 #count = count + 1

print("---------------")

#Using a while loop for user input validation
target_number = 12
while True:
    user_input = input("Guess the number: ")
    user_guess = int(user_input)
    
    if user_guess == target_number:
        print(f"Your guess was right: {user_guess}")
        break
    else:
        print("Invalid input. Guess again.")

print("---------------")
    
# Use of break in if statement
"""
It can only be used inside a loop to break the loop. In a simple if statement 
it has no point because it's not inside any loop to break out of. Using break 
outside of a loop will result in a SyntaxError.
"""
count = 0
while True:
    count += 1 #count = count + 1
    print(f"Count is: {count}")
    if count == 5:
        print("Reached 5. Breaking the loop.")
        break
print("Loop has ended.")

print("---------------")

nums = [1,2,3,4,5,6,7,8,9,10]
for i in nums:
    if (i == 5):
        break
    print(i);
print("Reached 5. Breaking the loop.")