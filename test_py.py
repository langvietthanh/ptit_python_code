from collections import namedtuple,defaultdict,OrderedDict

# def fun(s):
#     dic = defaultdict(list)
#     for i in range(len(s)):
#         dic[s[i]].append(i) 
#     if len(dic['@'])==0 or len(dic['@'])>1 : print(1); return False
#     if len(dic['.'])==0 or len(dic['.'])>1 or (len(dic['.'])==1 and dic['.'][0]< dic['@'][0]): print(2);return False
#     return True

s= input()

s= (filter(lambda s: '_' not in s, s ))
re = (s)
print (re)

