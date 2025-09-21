# Exercise 15: Equalizing Water in Three Containers

You are given three containers with initial amounts of water: `a`, `b`, and `c`.  

In each move, you can choose **any two containers** and transfer **any amount of water** (including fractional amounts) from one to the other.

Your goal is to make the amount of water **equal in all three containers** using the **minimum number of moves**.

### Input
A single line containing three integers:   
a,b,c

Constraints:  
0 ≤ a, b, c ≤ 10^15

### Output
Print a single integer — the **minimum number of moves** needed to equalize the water in all containers.

Example 1:
```
Input: 5 5 5
```
```
Output: 0
```

Example 2:
```
Input: 4 5 6
```
```
Output: 1
```

Example 3:
```
Input: 12 13 16
```
```
Output: 2
```

### Explanation
- If all containers already have the same amount → 0 moves.  
- If one container already has the target amount (average), one move is enough.  
- Otherwise, two moves are sufficient.
