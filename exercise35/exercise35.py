a = input()
b = int(input())
c = int(input())

num_10 = 0
for i in range(len(a)):
    digit = int(a[i])
    power = len(a) - 1 - i
    num_10 += digit * (b)**power

x = list()
while True:
    left = num_10 % c
    out = num_10 // c
    x.append(str(left))
    if out == 0:
        break
    else:
        num_10 = out

num_c = "".join(reversed(x))

def mirror(m):
    k = 0
    while True:
        k = (10 * k) + (m % 10)
        m = m //10
        if m == 0:
            break
    return k
if mirror(int(num_c)) == int(num_c):
    print("YES")
else:
    print("NO")               
