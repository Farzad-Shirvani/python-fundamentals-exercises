player1 = 0
player2 = 0
player3 = 0

while True:
    x, y, z = map(int, input().split())
    
    if x == y == z:
        break
    
    rolls = [x, y, z]
    min_roll = min(rolls)
    
    if rolls.count(min_roll) == 1:
        if min_roll == x:
            player1 += 1
        elif min_roll == y:
            player2 += 1
        else:
            player3 += 1

if player1 > player2 and player1 > player3:
    print("Player 1 is the champion!")
else:
    print("No champion for Player 1.")