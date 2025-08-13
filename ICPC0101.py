n = int (input())
lst = list(map(int,input().split()))
lst2 = []
for item in lst :
    if(lst2 and(item + lst2[-1])%2==0):
        lst2.pop()
    else :
        lst2.append(item)
print (len(lst2))

