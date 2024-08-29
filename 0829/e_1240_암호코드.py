import sys
sys.stdin = open('z3.txt' , 'r')

def checkpoint():
    for i in range(n):
        for j in range(m-1 , -1,-1):
            if int(arr[i][j]) :
                return (i,j)
    

password = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011',""]


for tc in range(1,int(input())+1):
    n,m = map(int,input().split())
    arr=[list(input()) for _ in range(n)]
    sr,sc = checkpoint()
    code = arr[sr][sc-55:sc+1]
    
    num_li =[]
    for i in range(0,56,7):
        po = "".join(code[i:i+7])
        num_li.append(password.index(po))
    # print(num_li)
    
    
    
    even_num =0
    odd_num =0

    for i in range(8):
        if i%2==0:
            even_num += int(num_li[i])
        else:
            odd_num += int(num_li[i])
    result = 0
    if (even_num*3 + odd_num )%10 == 0:
        result = even_num + odd_num
    else:
        result = 0
    print(f'#{tc} {result}')


    
