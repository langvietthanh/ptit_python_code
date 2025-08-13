n  = int(input())

for _ in range (n):
    s = input()
    stack = []
    for c in s:
        if(stack):
            if(stack[-1].isnumeric() and c.isnumeric()):
                num = stack[-1]+ c
                stack.pop()
                stack.append(num)
            else : stack.append(c)
        else : stack.append(c)
    ans = -1e18
    for item in stack: 
        if(item.isnumeric()):ans = max(ans,int(item))
    print (ans)