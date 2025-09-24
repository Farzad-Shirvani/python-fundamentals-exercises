# Exercise 24: Coordinate Spiral

A **coordinate spiral** starts at the origin `(0,0)` with the number `1`.  
The numbers are placed on the spiral as follows:

- `1 → (0,0)`
- `2 → (1,0)`
- `3 → (1,1)`
- `4 → (-1,1)`
- `5 → (-1,-1)`
- `6 → (2,-1)`
- `7 → (2,2)`
- `8 → (-2,2)`
- `9 → (-2,-2)`
- `10 → (3,-2)`

The path continues with the pattern: **right → up → left → down**,  
with segment lengths increasing after every two turns.


### Input
An integer `n` (`1 ≤ n ≤ 10^6`).

### Output
Two integers `x` and `y`, separated by a space, representing the coordinates of number `n`.

Example 1:
```
Input: 6
```
```
Output: 2 -1
```

Example 2:
```
Input: 11
```
```
Output: 3 3
```

Example 3:
```
Input: 13
```
```
Output: -3 -3
```
