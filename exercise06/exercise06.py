c = input()
n = int(input())

print(c * n)

for _ in range(3):
    print(c + ' ' * (n-2) + c)

print(c * n)