n, k = map(int, input().split())
a = list(map(int, input().split()))
count = 0
for i in a:
    if i > k:
        count +=1

if count >= 1:
    print("Yes")
else:
    print("No")            