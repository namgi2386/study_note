def counting_sort(data,temp,k):
    # data : 정렬 대상
    # temp : 정렬 결과
    # k : 정렬대상 중 최댓값
    # count : 등장원소 갯수 기록
    # count[x] : 원소 x 의 등장횟수

    count = [0] * (k+1)

    # 1. 원소 갯수 기록
    for num in data:
        count[num] += 1 # 숫자 num이 등장시 count의 num자리(num==index)에 1 더해줌

    # 2. 누적합 계산
    for i in range(1,len(count)):
        count[i] += count[i-1] # 앞선 숫자의 등장횟수를 누적합

    # 3. 뒤부터 data 확인 후 count 값에따라 자리배정
    # count값 -1 자리에 넣는다.
    # 뒤부터인 이유는 안정정렬(원래순서보장)을 위함
    for i in range(len(data)-1,-1,-1): # 끝인덱스 " len(data)-1 " 부터 첫인덱스 0 미만까지니까 -1 , 을 역순으로
        count[data[i]] -= 1 #맨끝숫자의 카운트 값을 하나줄이고
        idx = count[data[i]] # 맨끝숫자의 카운트값 == 누적합 == 정렬될 자리
        temp[idx] = data[i] #  정렬될 자리에 맨끝숫자 넣기

nums = [0,4,1,3,1,2,4,1]
result = [0]*8
counting_sort(nums,result,max(nums))
print(result)



