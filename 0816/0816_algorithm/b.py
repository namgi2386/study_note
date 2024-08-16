n,m = map(int,input().split())
visited =[0]*(n+1)
s =[]

def ee(num):
    if len(s)==m:
        print(*s)
        return

    for i in range(num,n+1):
        if i not in s:
            s.append(i)
            #visited[i]=1
            ee(i+1)
            s.pop()
            #visited[i]=0

ee(1)