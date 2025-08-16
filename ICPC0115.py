t = int (input())
dp = []
for i in range(10):
    if i < 2: 
        dp.append(1)
    else :
        dp.append(dp[i-1]*i)
for _ in range(t):
    n = input()
    s = 0
    for item in n: 
        num = int(item)
        s += dp[num]
    if str(s) == n:print("Yes")
    else : print ("No")
