n = int (input())
for _ in range(n):
    st = input()
    stack = []
    for item in st:
        if (stack):
            if (stack[-1].isnumeric() and item.isnumeric()):
                num = stack[-1] + item
                stack.pop()
                stack.append(num)
            else : stack.append(item)        

        else: stack.append(it)
    ans = 1e18
    
    for item in stack:
        if (item.isnumeric()):
            x = int(item)
            ans = min (ans , x)
    print (ans)

