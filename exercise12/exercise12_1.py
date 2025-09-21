a = int(input())
b = int(input())

a_1 = a % 10
a_2 = (a // 10) % 10
a_3 = (a // 100) % 10

b_1 = b % 10
b_2 = (b // 10) % 10
b_3 = (b // 100) % 10

a_ud = (a_1 * 100) + (a_2 * 10) + (a_3)
b_ud = (b_1 *100) + (b_2 * 10) + (b_3)

if a_ud > b_ud:
    print(f"{b} < {a}")
elif a_ud < b_ud:
    print(f"{a} < {b}")
else:
    print(f"{a} = {b}")