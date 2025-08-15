import itertools

if __name__ == '__main__':
    t = int(input())
    while (t):
        n,b= map(int,input().split())
        arr = list(map(int,input().split()))
        for i in range(b,n,1):
            print(arr[i],end=" ")
        for item in arr[:b]:
            print(item,end=" ")
        print()
        t-=1
    