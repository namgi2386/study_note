def are_u_same():
    result = 1
    for i in range(n): # 입력받은 배열의 각지점 탐색
        d = 1
        counts = 1                  # 기본 1점
        while 0<=(i-d) and (i+d)<n: # 좌우위치 범위 체크
            if arr[i-d] == arr[i+d]:  # 동일한지 체크
                counts += 2         # 동일하면 2점
            else:
                break               # 다르면 중단
            d += 1                  # 같으면 한칸 더 확인
        result = max(result , counts)       # 최댓값 갱신
    return result

for tc in range(1,int(input())+1):
    n = int(input())
    arr = list(map(int,input()))
    print(f'#{tc} {are_u_same()}')