import math
def check(n):
    if n==2 : return True
    if n<2 or (n%2==0): return False
    for i in range(3,math.isqrt(n)+1,2):
        if(n%i == 0) :return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t :
        n = input()
        m = n[::-1]
        s = sum (int(d) for d in n)
        if(check(int(n)) and check(s) and check (int(m)) and all(check(int(d)) for d in n) ):print("Yes")
        else : print ("No")
        t-=1

