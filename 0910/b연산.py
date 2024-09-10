from collections import deque

def hey_you(lev,num,visited):
    global result
    if num ==m:
        result = min(result , lev)
        return
    operator =[]
    if
    hey_you(lev+1,num+1,visited + [(lev+1,num+1)])

for tc in range(1,int(input())+1):
    n,m = map(int,input().split())
    result = 1e9
    visited =[[] for _ in range(1e7)]
    hey_you(0,n,[(0,n)])