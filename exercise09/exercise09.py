A, B, C = map(int, input().split())

if A > 0 and B > 0 and C > 0 and A + B + C == 180 and (A == 90 or B == 90 or C == 90):
    print("Yes")
else:
    print("No")