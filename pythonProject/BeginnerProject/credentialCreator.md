# Credential Creator (Deadline: March 06 11:59PM, 2021):

### Step1
First of all it will create some global variables to store letters (lowercase and 
uppercase), digits and punctuation respectively. You can use the following scripts
directly:
```
import string
lower_case=list(string.ascii_lowercase)
upper_case=list(string.ascii_uppercase)
digit=list(string.digits)
symbol=list(string.punctuation)
vowel=['a', 'i', 'e', 'o', 'u']
```
Use the random method to select character from above each list given.
It needs to use a mixture of numbers, alphabets and other symbols picked up
from above lists given to form a random credential string which is unpredictable 
and cannot easily be memorized.

1. The components of the credential are represented in the form of arrays.
2. The credential should start with a Vowel letter from above list.
3. The length of credential string was at least 12.
4. The credential contains at least one lower case letter.
5. The credential contains at least one upper case letter.
6. The credential contains at least one digit.
7. The credential contains at lease one symbol/punctuation.
8. It needs to create each independent function for above methods like select random vowel and so on
9. Finally, it needs to create a main function to call your every function.


Output :
```
af2byU$@zTg5
```

### Step2
Generate a string made of the first 2 and the last 2 characters from above credential:

Output :
```
afg5
```

### Step3
Count all lower case, upper case, digits, and special symbols from above credential:

Output :
```
Total counts of lower case, upper case, digits,and symbols 

LowerCase = 6 
UppderCase = 2 
Digits = 2 
Symbol = 2
```

### Step4
Remove special symbols/punctuation from above credential:

Output :
```
af2byUzTg5
```
