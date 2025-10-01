n , st = map(str, input().split())

def S_or_T(n, st):
    if st == "s" :
        n = int(n)
        for i in range(1, n+1):
            for j in range(1, n+1):
                print("*", end = "")
            print()    
    elif st == "t":
        n = int(n)
        for i in range(n, 0, -1):
            for j in range(i):
                print("*", end = "")
            print()    

S_or_T(n, st)                