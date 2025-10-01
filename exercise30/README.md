# Exercise 30: Decreasing Filled Squares

Given two integers `n` and `k`, and a character `c`, print a sequence of filled squares.  
- Start with a square of size `n × n` filled with character `c`.  
- After each square, decrease the size by `k` and repeat until the size is greater than zero.

### Input
A single line containing two integers `n` and `k` (1 ≤ k ≤ n ≤ 100) and a character `c`.

### Output
Print a sequence of filled squares as described above.

Example 1:
```
Input: 8 3 p
```
Output:
```
pppppppp
pppppppp
pppppppp
pppppppp
pppppppp
pppppppp
pppppppp
pppppppp
ppppp
ppppp
ppppp
ppppp
ppppp
pp
pp
```

Example 2:
```
Input: 9 3 *
```
Output:
```
*********
*********
*********
*********
*********
*********
*********
*********
*********
******
******
******
******
******
******
***
***
***
```
