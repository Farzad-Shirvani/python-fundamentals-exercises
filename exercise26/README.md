# Exercise 26: Strange Circle

There are `n` people sitting around a circle, numbered `1` to `n`.  
The game starts from person `1`. In each turn, the next person is chosen by moving `k` steps forward around the circle. The process continues until it returns to person `1`, at which point the game ends.  

Your task is to determine how many turns the game lasts.

### Input
Two integers `n` and `k` (1 ≤ k ≤ n ≤ 1000).

### Output
Print the number of turns until the game returns to person `1`.

Example 1:
```
input: 7 2
```
```
Output: 7
```
**Explanation (steps):**

Number the people from `1` to `7`, starting from person `1`. In each step we move `k = 2` positions forward.  
The sequence of people who play is:  
1 → 3 → 5 → 7 → 2 → 4 → 6 → 1

‌Example 2:
```
Input: 5 5
```
```
Output: 1
```
