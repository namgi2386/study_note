import sys
sys.stdin = open('z1.txt' , 'r')

def is_valid(nr , nc):
  return 0<=nr<n and 0<=nc<n

dr=[1,0,-1,0]
dc=[0,1,0,-1]

def tank():
  q =[(0,0)] # 시작지점 ( 0,0 ) 과 점수합계 0점
  visited = [[float('inf')]*n for _ in range(n)]
  visited[0][0] = 0

  while q:
    r,c = q.pop(0)

    if r==n-1 and c==n-1 : 
      if q:
        r,c=q.pop(0)
        pass
      else:
        return visited[r][c]

    for d in range(4):
      nr = r + dr[d] 
      nc = c + dc[d]
      if is_valid(nr,nc) :
        position_counts = maze[nr][nc] + visited[r][c] 
        if visited[nr][nc] > position_counts:
          visited[nr][nc] = position_counts
          q.append((nr,nc))

  return visited[n-1][n-1]





for tc in range(1,int(input())+1):
  n = int(input())
  maze=[list(map (int , list((input())) )) for _ in range(n)]
  print(f'#{tc} {tank()}')
