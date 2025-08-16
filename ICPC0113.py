import math 
maxn = int(10**6+1)
prime = [1 for _ in range (maxn)]

def prime_number() : 
    prime [0] = 0
    prime [1] = 0
    for i in range (2, math.isqrt(maxn)):
        if prime[i] :
            for j in range (i*i,maxn,i): prime [j] = 0

if __name__ == '__main__' :
    t = int(input())
    prime_number()
    for _ in range(t):
        n = int(input())
        for i in range (n):
            ir = "".join(reversed(str(i)))
            # print (ir)

            if prime[i] and prime[int(ir)] and int(ir) < n and int(ir) > i : print (i , ir ,end=" ")
        print ();
