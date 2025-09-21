n = int(input())
m = int(input())

coords = {1:(0,0), 2:(1,0), 3:(0,1), 4:(1,1)}

x1, y1 = coords[n]
x2, y2 = coords[m]

print(abs(x1-x2) + abs(y1-y2))