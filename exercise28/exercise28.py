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
    x = gcd_2(m_1, m_2)
    x = gcd_2(x, m_3)
    x = gcd_2(x, m_4)
    x = gcd_2(x, m_5)
    return x    
    
print(gcd_5(a, b, c, d, e))    
    
