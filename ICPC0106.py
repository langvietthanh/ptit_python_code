
def base_4 (s):
    num = int(s,2)
    ans = ""
    if(num == 0): return "0";
    while(num) :
        ans =str(num%4)+ans
        num //= 4; 
    return ans

n = int (input())

for _ in range (n):
    b = int (input())
    s = input()
    num_hex = int(s,2)
    if(b==2): print(bin(num_hex)[2:])
    elif(b==4): print(base_4(s))
    elif(b==8): print(oct(num_hex)[2:])
    elif(b==10): print(num_hex)
    elif(b==16): print(hex(num_hex)[2:].upper())