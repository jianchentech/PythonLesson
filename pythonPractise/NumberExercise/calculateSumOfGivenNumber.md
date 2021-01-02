# Exercise:

Accept number from user and calculate the sum of all number between 1 and given number
For example user given 10, so the output should be 55

#Eric Solution
```
number = input("input a number:")
int_number = int(number)
result = (1+int_number)*int_number/2
int_result = int(result)
str_result = str(int_result)
print(str_result)
```