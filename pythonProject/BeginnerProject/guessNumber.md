# Number Guessing Game (Deadline: January 30 11:59PM, 2021):

This project also uses the random module in Python. The program will first randomly generate a number unknown to the user. The user needs to guess what that number is. (In other words, the user needs to be able to input information.) If the user’s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high or too low). If the user guesses correctly, a positive indication should appear. It needs to check the difference between the inputted number and the randomly generated numbers, and then compare the numbers.
Concepts to keep in mind:
```
Random function
Variables
Integers
Input/Output
Print
While loops
If/Else statements
```

## Requirement:

- User inputs the **lower bound** and **upper bound** of the range.
- User input the maximum number of guesses.
- The program generates a random integer between the range.
- For repetitive guessing, a while loop will be initialized.
- If the user guessed a number which is greater than a randomly selected number, the user gets an output “Try Again! You guessed too high“
- If the user guessed a number which is smaller than a randomly selected number, the user gets an output “Try Again! You guessed too small”
- If the user guessed within the maximum number of guesses, the user gets a “Congratulations! ” Output.
- If the user didn’t guess the integer with the maximum number of guesses, he/she will get “Better Luck Next Time!” output.

# Eric Section:
### Solution:
```
import random
lower_bound = int(input("input the lower bound of the range:"))
upper_bound = int(input("input the upper bound of the range:"))
maximum_number_of_guesses = int(input("input the maximum number of guesses:"))
y = 0
if upper_bound < lower_bound:
    print("The upper bound of the range should be bigger than the lower bound of the range.")
else:
    x = random.randrange(lower_bound, upper_bound)
    while maximum_number_of_guesses > 0:
        Guess = int(input("What is your guess:"))
        if Guess > x:
            print("Try Again! You guessed too high.")
        elif Guess < x:
            print("Try Again! You guessed too small.")
        elif Guess == x:
            print("Congratulations!")
            y = 1
            break
        maximum_number_of_guesses = maximum_number_of_guesses-1
        print("")
    if y != 1:
        print("Better Luck Next Time!")
```
### Results:
```
input the lower bound of the range:1
input the upper bound of the range:10
input the maximum number of guesses:3
What is your guess:5
Try Again! You guessed too small.

What is your guess:8
Try Again! You guessed too small.

What is your guess:9
Congratulations!
```
### Code Review: 
```
The project was developed according to acceptance criteria and the skeleton
of structure looks good for the code. Some issue still need to be corrected
as followed:
1. The statement 'import random' should be placed on the top of whole program
2. After each try, the random number generated by the computer can't be outputted and 
shown to the user, otherwise it is not a guessing game. Because in each try, the 
user shouldn't know the random number generated by the computer.
3. It needs to fix the random number created by the computer, if the number changes
during each try, it will be very difficult for the user to find the guess number.
Excellent Job!
```
----
# Helen Section:
### Solution:
```
import random
print("""******Number Guessing Game******
""")
a = int(input("Input the upper bound in range:"))
b=int(input("Input the lower bound in range:"))
c = int(input("Input the number of guesses:"))
if b>a:
    print("The lower bound needs to be smaller than the upper bound")
else:
    e=random.randrange(b, a)
    n=0
    while n<c:
        d = int(input("Input your guess:"))
        n=n+1
        if d>e:
            print("Try Again! You guessed too high")
        elif d<e:
            print("Try Again! You guessed too small")
        elif d==e:
            print("Congratulations!")
            break
```
### Results:
```
******Number Guessing Game******

Input the upper bound in range:10
Input the lower bound in range:1
Input the number of guesses:3
Input your guess:5
Try Again! You guessed too high
Input your guess:3
Congratulations!
```
### Code Review: 
```
The project was developed according to acceptance criteria and the skeleton
of structure looks good for the code. However some scenarios were not considered,
for example: if the gussing number chance overpass the maxmium value, it should
output indication to user.
Excellent Job! 
```
----
# Jeremy Section:
### Solution:
```
import random
n=int(input("enter your number limit:"))
number = random.randrange(1,n)
guess = int(input("guess a number between 1 and n:"))
while guess != number:
    if guess< number:
        print("your guess is too low.😥 Try again")
        guess = int(input("guess a number between 1 and n: "))
    elif guess>number:
        print("your guess is too high.😥Try again")
        guess = int(input(" guess a number between 1 and n: "))
else:
    print("you guessed the number correctly!Congratulations!🙂🤗😊👏😜")
```
### Results:
```
enter your number limit:10
guess a number between 1 and n:5
your guess is too low.😥 Try again
guess a number between 1 and n: 8
you guessed the number correctly!Congratulations!🙂🤗😊👏😜
```
### Code Review: 
```
This project has been developed according to user requirements and the code
structure is clear. The combination of while loop and if else conditions
were mastered. Especially your usage of childlike emoji symbols really 
impressed me. But the following requirements were not reflected in your
program:
- User inputs the **lower bound** and **upper bound** of the range.
- User input the maximum number of guesses.
- If the user didn’t guess the integer with the maximum number of guesses, he/she will get “Better Luck Next Time!” output.
Furthermore, this lined code 'guess = int(input(" guess a number between 1 and n: "))'
was repeated with 3 time and you can simplify it for optimization.
If you can continue your progress and will definitely reach your final goal.
```
----
# Vincent Section:
### Solution:
```
from random import randint

value = randint(0, 10)
print("A random number between 0 and 10 has been generated")

number  = input("Guess the number:")

if  int(number) < value:
    print("Almost, but too small")

if int(number) == value :
    print("Good job!")

if int(number) > value:
    print("Too high!")

if int(number) > 10:
    print("Way too high!")
```
### Results:
```

```
### Code Review: 
```
The program was developed but only partial functinality were realized. For 
finishing the whole project, the following key requirements still need to be
designed and implemented according to acceptance criteria:
- User inputs the **lower bound** and **upper bound** of the range.
- User input the maximum number of guesses.
- For repetitive guessing, a while loop will be initialized.
In addition, it need to use if else conditions instead of only 4 if conditions.
Apparently, the concept of condition in Python was still very clear
It is still far from the final objective of this project. 
Anyway, if you work hard and continue to improve your code, you will be
successful finally.
```
----
# Vivianne Section:

### Solution:
```

```
### Results:
```

```
### Code Review: 
```

```