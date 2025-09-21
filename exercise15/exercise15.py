a, b, c = map(int, input().split())

target = (a + b + c) / 3

equal_to_target = sum([a == target, b == target, c == target])

if equal_to_target == 3:
    print(0)
elif equal_to_target >= 1:
    print(1) 
else:
    print(2)