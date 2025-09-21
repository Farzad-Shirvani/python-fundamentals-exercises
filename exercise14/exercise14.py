a, b, c, d, e, f = map(int, input().split())

ice = sorted([d, e, f])  
smallest, middle = ice[0], ice[1]

if (a >= middle and b >= smallest) or (b >= middle and a >= smallest):
    print("Yes")
else:
    print("No")