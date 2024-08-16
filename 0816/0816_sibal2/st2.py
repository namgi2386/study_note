# T = int(input())
# for tc in range(1,T+1):
#     n = int(input())
#     arr = list(map(int,input().split()))
#
#     arrd = []
#     arrd.extend(arr)
#     arrd.extend(arr)
    # 0 1 1 1 0 0 1
    # 1 1 3 2

counts = 0
i = -1
li =[]
c= 0
arrt = [0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1]
while counts != 7:
    i +=1
    if arrt[i]==1:
        li.append(1)
        c=0
    else:
        c += 1
print(li)










arrt = [0, 1, 1, 1, 0, 0, 1,       0, 1, 1, 1, 0, 0, 1]
for i in range(14):
    if arrt[i] ==1 :

