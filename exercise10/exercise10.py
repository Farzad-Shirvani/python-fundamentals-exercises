a, b, c = input().split()
discount = 0

if "s" in (a, b, c):
    discount += 10
if "7" in (a, b, c):
    discount += 5
if "*" in (a, b, c):
    discount += 30

print(discount)