# Exercise 10: Discount Code

Write a program that reads 3 characters (separated by spaces).  
The discount is calculated as follows:
- If at least one character is `s`, add 10%.
- If at least one character is `7`, add 5%.
- If at least one character is `*`, add 30%.  
Extra occurrences of the same character do not increase the discount.  

Input: Three characters separated by spaces.

Output:
- Print the total discount percentage as an integer.

Example 1:
```
Input: s 7 *
```
```
Output: 45
```

Example 2:
```
Input: 7 k *
```
```
Output: 35
```

Example 3:
```
Input: s s s
```
```
Output: 10
```
