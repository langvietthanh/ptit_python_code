import math 
maxn = int(10**6+1)
prime = [1 for _ in range (maxn)]

def prime_number() : 
    prime [0] = 0
    prime [1] = 0
    for i in range (2, math.isqrt(maxn)):
        if prime[i] :
            for j in range (i*i,maxn,i): prime [j] = 0
    
t = int(input())
for _ in range (t):
    n = int (input())
    res = 0 
    prime_number()
    for i in range(n) :
        if i+2 >= n or i+4 >= n or i+6 >= n : continue
        if(prime[i] and prime[i+6] and prime[i+4] ) : res +=1
        elif(prime[i] and prime[i+6] and prime[i+2]) : res +=1
    print (res)