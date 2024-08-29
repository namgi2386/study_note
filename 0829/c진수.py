

def DecimalToBinary(num):
    binary_num =""

    if num ==0:
        return '0'
    while num > 0 :
        r = num%2
        binary_num = str(r) + binary_num
        num = num//2
    
    return binary_num


for tc in range(1,11):
    li=[]
    arr=list(input())
    n = len(arr)
    for i in range(n//7):
        # arr[7*i:7*(i+1)]
        h=0
        temp_result =0 
        for j in range(6,-1,-1):
            temp_result += (2**h)*int(arr[7*i:7*(i+1)][j])
            h+=1
        li.append(temp_result)
    print(*li)

'''
11111110000000000000100000101111110
[127, 0, 1, 2, 126]
'''