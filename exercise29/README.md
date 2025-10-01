# Exercise 29: Shape Drawer

Given an integer `n` and a character `s` or `t`, print a square or a triangle made of asterisks (`*`).

- If the character is `s`, draw a square of size `n × n`.
- If the character is `t`, draw a right-angled triangle with side `n`, starting with `n` asterisks in the first row and decreasing by one in each subsequent row.

### Input
A single line containing an integer `n` (1 ≤ n ≤ 100) and a character `s` or `t`.

### Output
Print the corresponding square or triangle pattern using `*`.

Example 1:  
Input: 
```
7 t
```
Output:  
```
*******
******
*****
****
***
**
*
```

Example 2:  
Input:
```
4 s
```
Output:
```
****
****
****
****
```
