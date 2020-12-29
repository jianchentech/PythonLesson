# Exercise:

Print multiplication table of given number
For example num = 2, so the output should be
```
2
4
6
8
10
12
14
16
18
20
```
# Helen Solution
```
a=int(input("Input a number:"))
for i in range(1, 13):
    print(i*a)
```