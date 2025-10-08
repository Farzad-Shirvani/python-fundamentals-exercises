# Exercise 33: Special Phone Numbers

A phone number is an 8-digit number that does not start with zero.
A number is called special if it satisfies at least one of the following conditions:

- Some digit appears at least 4 times.
- There exist three consecutive equal digits.
- The number is a palindrome (reads the same forward and backward).

### Input

The first line contains an integer t — the number of phone numbers.  
Each of the next t lines contains an 8-digit string that does not start with 0.

Constraints: `1 ≤ t ≤ 1000`

### Output

For each number, print:
- `Yes` if the number is special.
- `No` otherwise.

Example 1:  
Input:
```
5
11111111
12345678
34666825
12344321
17544721
```
Output:
```
Yes
No
Yes
Yes
No
```

