'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

n = int(input())
arr = list(map(int,input().split()))

cleft = [0]*(n+1)
cright = [0]*(n+1)

for i in range(n-1):
    parent = arr[i*2]
    child = arr[i*2+1]

    if cleft[parent] == 0:
        cleft[parent] = child
    else:
        cright[parent] = child

def preorder(t):
    if t:
        print(t , end=" ")
        preorder(cleft[t])
        preorder(cright[t])
def inorder(t):
    if t:
        inorder(cleft[t])
        print(t , end=" ")
        inorder(cright[t])
def postorder(t):
    if t:
        postorder(cleft[t])
        postorder(cright[t])
        print(t , end=" ")

preorder(1)
print()
inorder(1)
print()
postorder(1)