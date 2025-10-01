a, b, c, d, e = map(int, input().split())

def gcd_2(n_1,n_2):
    while True:
        r = n_1 % n_2
        if r == 0 :
            break
        n_1 = n_2
        n_2 = r  
    return n_2    
    
def gcd_5(m_1, m_2, m_3, m_4, m_5):
    numbers = [m_1, m_2, m_3, m_4, m_5]
    sorted_numbers = sorted(numbers)
    x = gcd_2(sorted_numbers[4],sorted_numbers[3])
    numbers_1 = [sorted_numbers[0], sorted_numbers[1], sorted_numbers[2],x]
    sorted_numbers_1 = sorted(numbers_1)
    y = gcd_2(sorted_numbers_1[3], sorted_numbers_1[2])
    numbers_2 = [sorted_numbers_1[0], sorted_numbers_1[1],y]
    sorted_numbers_2 = sorted(numbers_2)
    z = gcd_2(sorted_numbers_2[2],sorted_numbers_2[1])
    numbers_3 = [sorted_numbers_2[0], z]
    sorted_numbers_3 = sorted(numbers_3)
    return gcd_2(sorted_numbers_3[1],sorted_numbers_3[0])
    
print(gcd_5(a, b, c, d, e))  