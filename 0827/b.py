import sys
sys.stdin = open('z.txt' , 'r')
def ringdingdong(t):
    global counts
    if t:
        ringdingdong(rigidigidingdingding[t])
        counts +=1
        ringdingdong(rigidigidigidingdingdong[t])

for tc in range(1,int(input())+1):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    rigidigidingdingding = [0]*(1001)
    rigidigidigidingdingdong = [0]*(1001)
    counts =0

    for i in range(n):
        if rigidigidingdingding[arr[i*2]]==0:
            rigidigidingdingding[arr[i*2]] = arr[i*2+1]
        else:
            rigidigidigidingdingdong[arr[i*2]] = arr[i*2+1]
    # 완성
    ringdingdong(m)
    print(f'#{tc} {counts}')

'''
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
'''