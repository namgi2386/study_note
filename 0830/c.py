patton =[13,19,60,50,35,56,11,62,25,48]
arr = ['0']*6
result =[]
arr.extend(list(bin(int(input(),16))[2:]))
# print(arr)
for i in range(len(arr)-7):
    a = "".join(arr[i:i+6])
    # print(int(a,2))
    if int(a,2) in patton:
        result.append(patton.index(int(a,2)))
print(result)
