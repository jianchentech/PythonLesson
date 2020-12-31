# Exercise: 
Python program to display a given number is prime or not

### Note: 

A Prime Number is a whole number that cannot be made by multiplying other whole numbers

### Examples:

6 is not a Prime Number because it can be made by 2×3 = 6

37 is a Prime Number because no other whole numbers multiply together to make it.

### Given:

Input a number: 
37

### Expected output:

The Given number 37 is prime

#Eric Solution
```
str_number = input(("input a positive whole number__except 1:"))
int_number = int(str_number)
x = 0
for i in range(2, int_number):
    if int_number % i == 0:
        x = 1
if x == 1:
    print(str_number+" "+"is not prime.")
else:
    print(str_number+" "+"is prime.")
```