def home(t):                        # t와 연결된 친구들 모두 visited 체크하기
    visited[t] = 1
    while stack:
        t = stack.pop(0)
        for i in range(len(arr[t])):  
            if not visited[arr[t][i]]:
                visited[arr[t][i]] = 1
                stack.append(arr[t][i])
                home(arr[t][i])


for tc in range(1,int(input())+1):
    n , m = map(int,input().split())
    arr = [[] for _ in range(n+1)]
    visited =[0]*(n+1)
    visited[0] =1


    for i in range(m):                   # 양방향 그래프 만들기
        s,e = map(int,input().split())
        arr[s].append(e)
        arr[e].append(s)
    # arr 완성


    counts = 0
    while 0 in visited: # 모든 인원 체크할때까지 무한반복
        for i in range(n+1):
            if visited[i] == 0: # 시작!
                counts += 1     # 무리의 갯수 기록
                stack =[i]      # i번부터 시작해서 친구들 전부 찾기

                home(i)

                break
    print(f'#{tc} {counts}')