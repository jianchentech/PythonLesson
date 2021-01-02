# Mad Libs Generator:

Mad Libs Generator is the perfect project for beginners who are just starting out with software development. Primarily focused on strings, variables, and concatenation, this project will teach you how to manipulate user-inputted data. The program design is such that it will ask users to enter a series of inputs that will be considered as a Mad Lib. The input could be anything, an adjective, a noun, a pronoun, etc. Once all the inputs are entered, the application will take the data and arrange the inputs into a story template form. Sound fun?

# Solution:

```
""" Mad Libs Generator
----------------------------------------
"""
##Loop back to this point once code finishes
loop = 1
while (loop < 10):
## All the questions that the program asks the user
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun: ")
## Displays the story based on the users input
    print ("------------------------------------------")
    print ("Be kind to your",noun,"- footed", p_noun)
    print ("For a duck may be somebody's", noun2,",")
    print ("Be kind to your",p_noun,"in",place)
    print ("Where the weather is always",adjective,".")
    print ()
    print ("You may think that is this the",noun3,",")
    print ("Well it is.")
    print ("------------------------------------------")
## Loop back to "loop = 1"
    loop = loop + 1
```
