# Exercise:

Split a given string on hyphens into several substrings and display each substring

### Given:

str1 = Emma-is-a-data-scientist

### Expected Output:

Displaying each substring:
```
Emma
is
a
data
scientist
```
#Eric Solution:
```
str1 = "Emma-is-a-data-scientist"
split_str = str1.split("-")
for i in range(0, 5):
    print(split_str[i])
```