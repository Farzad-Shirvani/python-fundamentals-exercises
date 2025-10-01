n, k = map(int, input().split())

round_ = 0
i = 1
while True:
    i = (i + k) % n
    round_ += 1
    if i == 1:
        break

print(round_)
