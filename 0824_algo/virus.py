import sys
sys.stdin = open('z1.txt' , 'r')
def virus():
  s=[1]
  counts = 0
  visited =[0]*(n+1)
  while s:
    p = s.pop()
    visited[p]=1
    while arr[p]:
      w = arr[p].pop()
      s.append(w)
      if not visited[w]:
        visited[w]=1
        counts +=1

  return counts



n=int(input())
m=int(input())

arr = [[] for _ in range(n+1) ]
for i in range(m):
  a,b = map(int, input().split())
  # if a > b :
  #   a,b = b,a
  arr[a].append(b)
  arr[b].append(a)

print(virus())


