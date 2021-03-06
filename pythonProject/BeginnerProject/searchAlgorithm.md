# Search Algorithm (Deadline: March 20 11:59PM, 2021):

Given a list of integer numbers in range of 1 and 2000 as followed:
```
list_store=[2*i for i in range(1,1000)]
```
It needs user to enter a number and then search it in above given
listed integer numbers by using the following two search methods:

### Binary search
this search algorithm takes advantage of a collection of elements 
that is already sorted by ignoring half of the elements after just one
comparison. Write a function which implements binary search. It should take a list and number
entered by user as a parameter, and return the position of the number entered by user in the list. If the entered number is
not in the list, the function should return a message like 'The number was not existed
in Given list'.

```
1. Compare x with the middle element.
2. If x matches with the middle element, we return the mid index.
3. Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
4. Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.
```

### Linear search
Write a function which implements linear search. It should take a list and number
entered by user as a parameter, and return the position of the number entered by user in the list. If the entered number is
not in the list, the function should return a message like 'The number was not existed
in Given list'.

```
1. Start from the leftmost element of list and one by one compare x with each element of the list.
2. If x matches with an element, return True.
3. If x doesn’t match with any of elements, return False.
```
