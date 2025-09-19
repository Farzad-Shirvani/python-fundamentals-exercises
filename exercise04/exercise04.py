a, b = map(int,input().split())
a_mirror = (12-a)%12
b_mirrror = (60-b)%60
print(f"{a_mirror:02d}:{b_mirrror:02d}")