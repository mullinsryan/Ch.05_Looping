  #Sign your name: Ryan Mullins

'''
 1. Make the following program work.
   '''  
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    x = float(input("Enter a number: "))
    total = total + x
print("The total is:", total)
'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(2,101,2):
    print(i)
'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
count = 10
while count >= 0:
    print(count)
    count -= 1
print("Blast Off")
'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random

x = 0
while x < 1:
    numb = random.randrange(1,10)
    print(numb)
    x += 1

'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
x = 0
total = 0
pos = 0
neg = 0
zero = 0
while x < 1:
    for i in range(7):
        numb = float(input("Please enter a number: "))
        total += numb
        if numb > 0:
            pos += 1
        elif numb == 0:
            zero += 1
        else:
            neg += 1
    print("The total is", total)
    if pos == 1:
        print("There was 1 positive number.")
    else:
        print("There were", pos, "positive numbers")
    if neg == 1:
        print("There was 1 negative number")
    else:
        print("There were", neg, "negative numbers.")
    if zero == 1:
        print("There was", zero, "zero.")
    else:
        print("There were", zero, "zeroes.")
    x += 1