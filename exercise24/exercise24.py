def spiral_coord(m):
    if m == 1:
        print("0 0")
        return  

    x, y = 0, 0 
    s = m - 1   

    for t in range(1, s + 1):
        length = (t + 1) // 2  
        if t % 4 == 1:   
            x += length
        elif t % 4 == 2: 
            y += length
        elif t % 4 == 3:
            x -= length
        else:            
            y -= length

    print(f"{x} {y}")   

n = int(input())
spiral_coord(n)  
