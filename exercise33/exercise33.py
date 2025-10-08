t = int(input())


def four(m):
    for i in m:
        if m.count(i) >= 4:
            return 1
    return 0
              

def three_row(m):
    for i in range(len(m)-2):
        if m[i] == m[i + 1] == m[i + 2]:
            return 1
    else:
        return 0


def mirror(m):
    m = int(m)
    k = 0
    while True:
        k = (10 * k) + (m % 10)
        m = m // 10
        if m == 0 :
            break
    return k


for i in range(t):
    m = input()
    if four(m) == 1 or three_row(m) == 1 or mirror(m) == int(m):
        print("Yes")
    else:
        print("No")    
        