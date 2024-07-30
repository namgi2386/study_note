
data = [0,4,1,3,1,2,4,1]
max_num =5
counts = [0]*max_num
counts_idx = [0]*max_num

n = len(data)
temp =[0]*n

# 1
for x in data :
    counts[x] += 1      #   counts = [ 1 , 3 , 1 , 1 , 2 ]

for i in range(n):
    counts_idx[data[i]] += 1

#2
for i in range(1,max_num):
    counts[i] += counts[i-1]     #  counts = [ 1, 4 , 5 , 6 , 8 ]

for x in counts[:n-1]:
    pass            #############?????????????????????

#3
for i in range(n-1,-1,-1):
    counts[data[i]] -= 1
    idx = counts[data[i]]
    temp[idx] = data[i]

### ???

print(temp)
