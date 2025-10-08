n = int(input())

def prime(n):
    if n < 2:
        return 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1       

        
def super_prime(n):
    s = str(n)
    for i in range(1, len(s)+1):
        if not prime(int(s[:i])):
            return 0
    return 1


number = 1
counter_3 = 0
while True:
    number += 1
    if super_prime(number) == 1:
        counter_3 += 1
        if counter_3 == n:
            print(number)
            break


