# 4개중 3개뽑기
for i1 in range(1,4):
    for i2 in range(1,4):
        if i2 != i1:
            for i3 in range(1,4):
                if i3 != i1 and i3 != i2:
                    print(i1,i2,i3)

'''
li = [1,2,3,7,7,7]
pectorial = 6*5*4*3*2*1
matrix = [[0]*7 for _ in range(pectorial)]
for i in range(pectorial):
    matrix[i] =
'''

# baby gin
num = 456789
c = [0] * 12
for i in range(6):
  c[ num % 10 ] += 1
  num //= 10


i =0
tri = run = 0
while i < 10 :
    if c[i] >= 3:
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2 : print("baby gin")
else : print("lose")