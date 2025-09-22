# Exercise 20: Dice Competition

Three players compete in a dice game:  

- In each round, everyone rolls a die once.  
- The player with the **smallest number** receives **1 point**.  
- If **two or more players tie for the smallest number**, **no points** are awarded.  
- The game ends when **all three dice show the same number**.  

Given the dice rolls of each round, determine if **Player 1** is the overall winner (has strictly the highest score).  

**Input:**  
- Each line contains three integers `x y z` — the dice results of Player 1, Player 2, and Player 3 in that round.  
- Input continues until a round where all three numbers are equal.  

**Output:**  
- If Player 1 wins, print: `Player 1 is the champion!`
- Otherwise, print: `No champion for Player 1.`

Example 1:  
Input:
```
1 6 4
3 3 5
4 1 2
1 2 3
2 2 2
```
Output:
```
Player 1 is the champion!
```

Example 2:  
Input:
```
5 2 1
3 3 5
2 4 6
1 1 1
```
Output:
```
No champion for Player 1.
```

