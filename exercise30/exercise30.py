n, k, c = map(str, input().split())
n = int(n)
k = int(k)

def n_k_square(n, k, c):
    for i in range(n):
        for j in range(n):
            print(c, end = "")
        print()
    while n - k > 0 :
        n = n - k 
        for i in range(n):
            for j in range(n):
                print(c, end = "")
            print()
            
n_k_square(n, k, c)            