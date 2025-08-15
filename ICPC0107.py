
a = 0
b = 0

def sum(s1,s2):
    n=len(s1)
    m=len(s2)
    if(n > m):
        tmp = s1
        s1 = s2
        s2 = tmp
    elif (s1>s2):
        tmp = s1
        s1 = s2
        s2 = tmp
    #  s1 < s2
    k = abs(n-m)
    s1 = ("0"*k) + s1
    reversed(s1)
    reversed(s2)
    du = 0
    res = ""
    for i in range(len(s2)):
        n1,n2 = int(s1[i]), int(s2[i])
        num = n1 + n2 + du
        # print (num)
        du = num // 10
        res = str(num%10)+ res
    if(du):res = str(du) + res
    return res

def sum_min (s1,s2):
    s3=""
    s4=""
    for item in s1:
        if( item == str(b) ): 
            s3 = s3 +  str(a)
        else: s3 = s3  + item
    for item in s2:
        if(item == str(b) ):
            s4 = s4 + str(a)
        else: s4 = s4 + item
    return sum(s3,s4)

def sum_max (s1,s2):
    s3=""
    s4=""
    for item in s1:
        if( item == str(a) ): 
            s3 = s3 +  str(b)
        else: s3 = s3  + item
    for item in s2:
        if(item == str(a) ):
            s4 = s4 + str(b)
        else: s4 = s4 + item
    return sum(s3,s4)

if __name__ == '__main__':
    n  = int(input())
    for _ in range(n):
        a,b = map(int,input().split())
        if(a>b):
            tmp = a
            a=b
            b=tmp
        s1 = input().strip()
        s2 = input().strip()
        print (sum_min(s1,s2),sum_max(s1,s2),sep = "  ")