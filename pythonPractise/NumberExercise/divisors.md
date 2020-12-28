# Exercise:
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
If you don’t know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# Eric Solution:

```
print('Input a number:')
number = input()
print('The divisors of your number are:')
for i in range(1, int(number) +1):
    if int(number) % i == 0:
        print(i)
```