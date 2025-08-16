
a = 0
b = 0

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
    return int(s3) + int(s4)

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
    return int(s3) + int(s4)

if __name__ == '__main__':
    n  = int(input())
    for _ in range(n):
        a,b = map(int,input().split())
        if(a>b):
            tmp = a
            a=b
            b=tmp
        s1 = input()
        ele = len(s1.split())
        if(ele >1): s1 ,s2 = s1.split()
        else : s2 = input()
        print (sum_min(s1,s2),sum_max(s1,s2),sep = " ")