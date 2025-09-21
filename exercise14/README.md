# Exercise 14: Placing a Ice Cuboid in a Box

You have found a **rectangular ice cuboid** and a **box with an open top**. You want to place the ice in the box so that it will fully melt inside.

- Ice dimensions: `d × e × f`  
- Box dimensions: `a × b × c` (open top, base: `a × b`)  

> Note: The ice cuboid can be rotated, but its edges must remain parallel to the edges of the box. The height of the ice cuboid does **not** matter and can exceed the height of the box. Only the base dimensions need to fit inside the box.

### Input
A single line containing six positive integers:  
a,b,c,d,e,f

Constraints: 
1≤a,b,c,d,e,f≤10^18


### Output
- Print `YES` if the ice cuboid **can fit in the box**.  
- Print `NO` if it **cannot fit**.

Example 1:
```
Input: 1 100 100 2 1 200
```
```
Output: Yes
```
Example 2:
```
Input: 111111111111 333333345 2334 333333345 222222222222 1111111111
```
```
Output: Yes
```

Example 3:
```
Input: 4 4 100 95 3 100
```
```
Output: No
```

### Explanation
- The ice cuboid can be **rotated** to fit.  
- The ice cuboid fits if **its base dimensions are less than or equal to the box's base dimensions** (length and width), considering rotation.  
- The height does not matter.
