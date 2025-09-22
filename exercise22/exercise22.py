n = int(input())

total_sum = 0

for i in range(1, n + 1):
    current_sum = 0
    for j in range(1, i + 1):
        current_sum += j
        total_sum += j
        if j < i:
            print(j, end="+")
        else:
            print(j, end=" ")
    print("=", current_sum)

print("Total sum of series is:", total_sum)