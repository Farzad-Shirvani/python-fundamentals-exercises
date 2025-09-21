# Exercise 13: Minimum Moves on 4 Points

There are 4 points numbered 1 to 4 forming a square:
```
1 --- 2
|     |
|     |
3 --- 4
```
<img width="250" height="1024" alt="deb7f81d-349a-456f-a55b-4385f5f1e68e" src="https://github.com/user-attachments/assets/b8e79149-1b65-4ca5-b4d1-0a89f6493078" />

You start at point `n` and want to reach point `m`.  
You can move **one unit up, down, left, or right** per move.  
If you move outside the square from a corner, you fall and cannot return.

Calculate the **minimum number of moves** needed to reach from `n` to `m`.

Input:  
  Two lines:  
  - Line 1: integer `n` (starting point)  
  - Line 2: integer `m` (target point)  

  Constraints:  
  1 ≤ n,m ≤ 4

Output: One integer: the minimum number of moves.
