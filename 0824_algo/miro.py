import sys
sys.stdin = open('z1.txt' , 'r')

def is_valid(nr , nc):
  return 0<=nr<n and 0<=nc<m

dr=[1,0,-1,0]
dc=[0,1,0,-1]

def miro():
  q= [(0,0)]
  visited =[[0]*m for _ in range(n)]
  visited[0][0]=1

  while q:
    r,c = q.pop(0) 

    for d in range(4):
      nr = r + dr[d] 
      nc = c + dc[d]
      if is_valid(nr,nc) and not visited[nr][nc] and arr[nr][nc] :
        q.append((nr,nc))
        visited[nr][nc] = visited[r][c] + 1
  
  return visited[n-1][m-1]

n,m=map(int,input().split())
arr = [list(map(int, input())) for _ in range(n)] 
print(miro())


