n = int(input())

n = str(n)

while True :
    sum_num = 0
    for i in n:
        sum_num = sum_num + int(i)
    if sum_num // 10 > 0 :
        n = sum_num 
        n = str(n)
    else :
        break
print(sum_num)
