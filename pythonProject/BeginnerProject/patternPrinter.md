# Pattern Printer (Deadline: January 16 12:00PM, 2021:

In Python, pattern printing programs are a great way to test nested loop designing skills. Essentially, all you have to do is print text in such a way, using loops, that they resemble symmetrical patterns.

## Step 1:
Now, if a user enters the number 5, you need to print five rows of the following Half Pyramid pattern. 
For example, a half pyramid pattern looks like this:

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5 
```
or
```
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
```
## Step 2:
You can try other patterns as well (at least two pattern) and create a menu-based program that asks the users which pattern they want to print. For instance like the following menu:

```
----------Pattern Printer Menu----------
1. Print Half Pyramid of Number
2. Print Inverted Half Pyramid of Number
3. Print full Pyramid of Number
4. Print Inverted full pyramid of Number
```
----
# Eric Section:
### Solution:
```
print("----------Pattern Printer Menu----------")
print("1. Print Half Pyramid of Number")
print("2. Print Inverted Half Pyramid of Number")
print("3. Print full Pyramid of Number")
print("4. Print Inverted full pyramid of Number\n")
Option = input(("Chose an option:"))
int_Option = int(Option)
Number_of_rows = input(("Chose a whole number for the rows of your Pyramid:" ))
int_Number = int(Number_of_rows)
print("Here's your Pyramid:")
if int_Option == 1:
    for i in range(1, int(Number_of_rows)+1):
        for x in range(1, i+1):
            print(x, end=" ")
        print("")
elif int_Option == 2:
    for x in range(0, int(Number_of_rows)):
        for i in range(1, int(Number_of_rows)+1-x):
            print(i, end=" ")
        print("")
elif int_Option == 3:
    a = "  "
    for i in range(1, int(Number_of_rows)+1):
        print(a * (int(Number_of_rows) - i), end="")
        for x in range(1, i * 2):
            print(x, end=" ")
        print("")
elif int_Option == 4:
    a = "  "
    b = int(Number_of_rows)
    for i in range(1, b+1):
        print(a * (i - 1), end=" ")
        for x in range(1, b * 2):
            print(x, end=" ")
        b = b - 1
        print("")
else:
    print("(This option is not in the Pattern Printer Menu)")
```
### Results:
```
----------Pattern Printer Menu----------
1. Print Half Pyramid of Number
2. Print Inverted Half Pyramid of Number
3. Print full Pyramid of Number
4. Print Inverted full pyramid of Number

Chose an option:1
Chose a whole number for the rows of your Pyramid:5
Here's your Pyramid:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

Chose an option:2
Chose a whole number for the rows of your Pyramid:5
Here's your Pyramid:
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 

Chose an option:3
Chose a whole number for the rows of your Pyramid:5
Here's your Pyramid:
    1
   123
  12345
 1234567
 
Chose an option:4
Chose a whole number for the rows of your Pyramid:5
Here's your Pyramid:
123456789
 1234567
  12345
   123
    1
```
### Code Review: 
```
The whole project has been delevoped according to the requirement. The menu for user and logic is 
much clear. However there are some details need to be corrected.
For option 3, i.e. full Pyramid, one row less than expected. In addition,
within both results of options 3 and 4, there are no space between
different numbers, because in code the parameter end in print should 
be " " instead of "".
After correction, options 3 and 4 still have problems. Furthermore,
the variable int_Number = int(Number_of_rows) seems unuseful,
becaus it was not used in other code. Too much casting via
Int() make the code redundant.
Excellent Job!
```
----
# Helen Section:
### Solution:
```
n=int(input("Input the number of rows:"))
b=input("""************Pyramid Printer Menu****************
1. Print Half Pyramid of Number
2. Print Inverted Half Pyramid of Number
3. Print Full Pyramid of Number
4. Print Inverted Full Pyramid of Number

Input the corresponding number of the pattern you want to print:""")

if b=="1":
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

elif b=="2":
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
elif b=="3":
    for i in range(1, n + 1):
        print("  " * (n - i), end=" ")
        for j in range(1, i * 2):
            print(j, end=" ")
        print("")
else:
    for i in range(n, 0, -1):
        print("  " * (n - i), end=" ")
        for j in range(1, i * 2):
            print(j, end=" ")
        print("")
```
### Results:
```
Input the number of rows:5
************Pyramid Printer Menu****************
1. Print Half Pyramid of Number
2. Print Inverted Half Pyramid of Number
3. Print Full Pyramid of Number
4. Print Inverted Full Pyramid of Number

Input the corresponding number of the pattern you want to print:1
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

Input the corresponding number of the pattern you want to print:2
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1

Input the corresponding number of the pattern you want to print:3
         1 
       1 2 3 
     1 2 3 4 5 
   1 2 3 4 5 6 7 
 1 2 3 4 5 6 7 8 9
 
Input the corresponding number of the pattern you want to print:4
 1 2 3 4 5 6 7 8 9 
   1 2 3 4 5 6 7 
     1 2 3 4 5 
       1 2 3 
         1 
```
### Code Review: 
```
This project has been developed very well according to 
requirements. The structure of codes is pretty readable
and concise. Input and output were unstandable for user.
If some comments were added to explain the code and it
will be ideal. In addition, the scenario like input other
numbers like 5 or anything else was not considered. 
Excellent Job! 
```
----
# Jeremy Section:
### Solution:
```
list2= [5,4,3,2,1]
for i in range(0, 5):
    print(list2[i:])
    
n=int(input("enter number of row:"))
for i in range(n):
    for j in range(i+1):
     print(j+1,end=" ")
    print()
```
### Results:
```
[5, 4, 3, 2, 1]
[4, 3, 2, 1]
[3, 2, 1]
[2, 1]
[1]

enter number of row:5
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
```
### Code Review: 
```
The project was designed only according to the requirement in Step1 part and 
the second part not developed yet. The half pyramid and the inverted one can 
be obtained as expected. Within the first solution, it should input the number
of rows instead of a constant list as a variable. The first part only inspect 
the knowledge of for loop. The second part need to combine for loop and if else 
condition together. The program need to provide a menu or options for user. At
least two choices withi different pyramid pattern can be selected and four
patterns will be ideal.
If you can continue like this and will be successful finally 
```
----
# Vincent Section:
### Solution:
```

```
### Results:
```

```
### Code Review: 
```

```
----
# Vivianne Section:
### Solution:
```
for i in range(1, 12):
    for j in range(12-i):
        print(" ", end=" ")
    for j in range(1, i):
        print(j, end=" ")
    print("\n")
```
### Results:
```
                    1 

                  1 2 

                1 2 3 

              1 2 3 4 

            1 2 3 4 5 

          1 2 3 4 5 6 

        1 2 3 4 5 6 7 

      1 2 3 4 5 6 7 8 

    1 2 3 4 5 6 7 8 9 

  1 2 3 4 5 6 7 8 9 10 
```
### Code Review: 
```
The project was developed only according the requirement in Step1 part and 
the second part not implemented yet. The half pyramid can be obtained as expected,
However, some acceptance criteria was missing, for example the user need to
input the number of rows of pyramid. In addition, three for loops were redundant,
while 2 for loops will be enough. The first part only inspect the knowledge
of for loop. The second need to combine for loop and if else condition together.
The program need to provide a menu or options for user. At
least two choices withi different pyramid pattern can be selected and four
patterns will be ideal.
Anyway it's a good start and I believe that you can achieve success finally.
```