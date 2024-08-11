import sys
sys.stdin = open('z1.txt','r')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    passage_count = [0]*200
    for i in range(len(arr)):
        start_idx = (arr[i][0]-1)//2
        end_idx = (arr[i][1]-1)//2
        if end_idx < start_idx:
            start_idx , end_idx = end_idx , start_idx
        for h in range(start_idx,end_idx+1):
            passage_count[h] += 1
    print(passage_count)
    print(f'#{tc} {max(passage_count)}')