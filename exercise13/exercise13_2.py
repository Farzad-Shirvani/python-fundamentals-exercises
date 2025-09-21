n = int(input())
m = int(input())

if n == m :
    print(0)
elif (n == 1) :
    if m == 2 or m == 3 :
        print(1)
    else :
        print(2)    
elif (n == 2) :
    if (m == 1 or m == 4) :
        print(1)
    else :
        print(2)    
elif (n == 3) :
    if (m == 1 or m == 4) :
        print(1)
    else : 
        print(2)     
elif (n == 4) :
    if (m == 2 or m == 3) :
        print(1)
    else:
        print(2)