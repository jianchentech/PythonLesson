# Exercise:
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Helen Solution

```
name=(input("your name:"))
age=int(input("your age:"))
b=2020
d=100
c=int((d-age)+b)
print(name+" will be one hundred years old in "+str(c)+"")
```