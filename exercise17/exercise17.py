n = int(input())
m = 0
while True:
    m = m * 10 + (n % 10)
    n = n // 10
    if n == 0 :
        break
print(m)    
    