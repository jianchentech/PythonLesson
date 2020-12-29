# Exercise:

Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

### Expected Output:
```
Given list is  [10, 20, 33, 46, 55]
Divisible of 5 in a list
10
20
55
```
# Helen Solution
```
a=(10, 20, 33, 46, 55)
for item in a:
    if item%5==0:
        print(item)
```