w_1, w_2, w_3, w_4, w_5 = map(int, input().split())

first_loop = max(w_1 , w_2) 
second_loop = max(first_loop, w_3)
third_loop = max(second_loop, w_4) 
final = max(third_loop, w_5) 

if final == w_1 :
    print(1)
elif final == w_2 :
    print(2)
elif final == w_3 :
    print(3)
elif final == w_4 :
    print(4)
elif final == w_5 :
    print(5)

