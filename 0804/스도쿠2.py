import sys
sys.stdin = open("input.txt", "r")

def test(tc,arr,n,s):
    count_sudo = 0
    for i in range(n):
        for j in range(n-s+1):
            for h in range(s):
                if arr[i][j+h] == 0:
                    if tc==1:
                        print(f'가로방향 {i} {j} {h}')
                    break
            else :
                count_sudo += 1 
            for h in range(s):
                if arr[j+h][i] == 0:
                    if tc==1:
                        print(f'            세로방향 {j} {i} {h}')
                    break
            else :
                count_sudo += 1

    return f'#{tc} {count_sudo}'



T = int(input())
for tc in range(1,T+1):
    n , s = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    print( test(tc,arr,n,s) )
