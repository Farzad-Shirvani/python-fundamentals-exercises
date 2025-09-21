a = input().strip()
b = input().strip()

a_rev = int(a[::-1])
b_rev = int(b[::-1])

if a_rev > b_rev:
    print(f"{b} < {a}")
elif a_rev < b_rev:
    print(f"{a} < {b}")
else:
    print(f"{a} = {b}")