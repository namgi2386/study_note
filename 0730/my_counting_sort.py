data_list = [0, 5, 4, 3, 1, 4, 1, 1, 3, 2, 0, 1, 5, 4, 4, 4, 3 ]
max_num = 6
counts = [0]*max_num ## 0~5 총 6개   # 6은 data_list의 최댓값 -1 찾아야됨

######################################################

for x in data_list:
    counts[x] += 1
print(counts)

######################################################

for i in range(1,max_num -1 ):          # 누적합
    counts[i] += counts[i-1]
print()
print(counts)

######################################################
max_len = len(data_list)
temp_list = [0]*max_len

for i in range(max_len-1,-1,-1):
    counts[data_list[i]] -= 1
    temp_list[counts[data_list[i]]] =data_list[i]
print()
print(temp_list)