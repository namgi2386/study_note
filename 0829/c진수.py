

def binary(num):
    binary_num =""

    if num ==0:
        return '0'
    while num > 0 :
        r = num%2
        binary_num = str(r) + binary_num
        num = num//2
    
    return binary_num


for tc in range(1,11):
    arr=list(input())
    n = len(arr)
    for i in range(n//7):
        arr[7*i:7*(i+1)]
        for j in range()