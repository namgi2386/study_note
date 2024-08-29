import sys
sys.stdin = open('z4.txt' , 'r')

def jjum_o():
    global namba
    result = ""
    while len(result) <=12:
        if namba == 0.0:
            return result
        if namba*2 >= 1.0:
            result += '1'
            namba = namba*2 - 1
        else:
            namba = namba*2
            result += '0'
    return False


for tc in range(1,int(input())+1):
    namba = float(input())
    result = jjum_o()
    if result:
        print(f'#{tc} {result}')
    else: 
        print(f'#{tc} overflow')
