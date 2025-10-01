# Exercise 24: Last Remaining Item

There are 5 items, numbered from 1 to 5. The weight of item *i* is `wᵢ` (all weights are distinct).

In each step, the two items with the smallest indices are selected. The lighter one is removed, and the heavier one remains. This process continues until only one item is left.

Your task is to output the index of the last remaining item.

### Input
A single line containing 5 integers `w₁, w₂, …, w₅` — the weights of the items.  
Constraints: `1 ≤ wᵢ ≤ 100`, all distinct.

### Output
Print the index (1–5) of the last remaining item.

Example 1:
```
Input: 4 2 1 5 3
```
```
Output: 4
```

Example 2:
```
Input: 5 2 4 3 1
```
```
Output: 1
``` 
