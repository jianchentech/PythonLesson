# Exercise:

Reverse the following list using for loop
list1 = [10, 20, 30, 40, 50]

### Expected output:
```
50
40
30
20
10
```
# Helen Solution
```
list1 = [10, 20, 30, 40, 50]
for i in range(1, 6):
    print(list1[-i])
```