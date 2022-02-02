

from collections import Counter

n=int(input())
own=list(map(int,input().split(" ")))
cus=int(input())
size=[]
cost=[]
for i in range(cus):
    s,c=map(int,input().split(" "))
    size.append(s)
    cost.append(c)
    
# list own is converted to dict own -----here shoe size is the key
# and their freq are the values
own=Counter(own)
money=0

for i in range(len(size)):
    
    """check if the shoe size the cus wants is in our dict using               own.keys()
    if there check if still the stock exists----i.e freq!=0"""
    
    if size[i] in own.keys() and own[size[i]]>0:
        money+=cost[i]
        # decrement the freq by 1 ---update the value in the dict
        own[size[i]]-=1
        
print(money)
        
