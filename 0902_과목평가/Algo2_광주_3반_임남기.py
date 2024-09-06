def make_bin(x):
    num = ord(x)            # 입력받은 값을 ascii 코드로 변환
    result =""
    for i in range(8):      # 이진수 변환
        if num & (1<<i):
            result += '1'
        else:
            result += '0'
    rresult = "".join(reversed(result))
    return rresult

def set_bin(b):                 # 이진수를 중위순회 순서로 출력
    result = [ b[4],b[2],b[5],b[1],b[6],b[3],b[7]]
    return "".join(result)



for tc in range(1,int(input())+1):
    n = int(input())
    arr = list(input())

    result =[]
    for i in range(n):
        temp_password = make_bin(arr[i])        # 이진수로 변환
        particle_password = set_bin(temp_password) # 중위순회
        result.append(particle_password)

    print(f'#{tc} ',end="")
    print(*result)


