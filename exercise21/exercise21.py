for i in range(1, 11):
    for j in range(1, 11):
        if i > j :
            print(i * j, end = " ")
        elif i == j :
            print(0 , end = " ")
        elif i < j :
            print(-(i * j), end = " ")
    print()        