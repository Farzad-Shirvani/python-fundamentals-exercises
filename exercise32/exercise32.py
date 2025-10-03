n = input()

b = 0
for i in n:
    b += int(i)

def prime(m):
    count = 0
    for i in range(2,m):
        if m % i == 0:
            count += 1
    if count == 0:
        return 1


count_2 = 0
while True:
    n = int(n)
    n += 1
    if prime(n) == 1:
        count_2 += 1
        if count_2 == b:
            print(n)
            break

