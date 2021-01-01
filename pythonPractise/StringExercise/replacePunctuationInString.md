# Exercise:
From given string replace each punctuation with #

### Given:

str1 = '/*Jon is @developer & musician!!'

### Expected Output:
```
##Jon is #developer # musician##
```
# Helen Solution
```
a = '/*Jon is @developer & musician!!'
for i in a:
    if i=="/" or i=="*" or i=="@" or i=="&" or i=="!":
        a=a.replace(i, "#")
print(a)
```