# Exercise 22: Cumulative Sum Series

Given an integer `n`, generate a series of cumulative sums as follows:  

- The 1st term is `1`,  
- The 2nd term is `1 + 2`,  
- The 3rd term is `1 + 2 + 3`,  
- …  
- The nth term is `1 + 2 + 3 + … + n`.  

Your task is to print the sum of each term and the **total sum** of all terms.

**Input:**  
- A single integer `n`  
- Constraint: `1 ≤ n ≤ 1000`

**Output:**  
- For each term `i` (from 1 to n), print:  
1+2+…+i = <sum_of_i>
- In the last line, print:
Total sum of series is: <total_sum>

Example 1:
```
Input: 5
```
Output:
```
1 = 1
1+2 = 3
1+2+3 = 6
1+2+3+4 = 10
1+2+3+4+5 = 15
Total sum of series is: 35
```

Example 2:
```
Input: 10
```
Output:
```
1 = 1
1+2 = 3
1+2+3 = 6
1+2+3+4 = 10
1+2+3+4+5 = 15
1+2+3+4+5+6 = 21
1+2+3+4+5+6+7 = 28
1+2+3+4+5+6+7+8 = 36
1+2+3+4+5+6+7+8+9 = 45
1+2+3+4+5+6+7+8+9+10 = 55
Total sum of series is: 220
```

**Note:**  
- Each line shows the sum of numbers from 1 up to `i`.  
- The last line gives the total sum of all these sums.  
- There is no input other than the single integer `n`.
