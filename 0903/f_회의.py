arr = [(5,50),(10,60),(20,140)]

# 단순한 한개의 값이 아닌 여러개의 값을 가진 구조를 정렬
# 이 여러개의 값들 중에 우리가 사용하고 싶은 정렬 기준이 뭔가

# 정렬 기준이 기본적으로 제공되는 타입들 이외에
# 다른것들은 직접 정렬 기준을 정해야함
# sort 함수의 key 인자를 활용하여 어떤 것을 기준으로 정렬할지 함수로 작성

# kg당 가치를 기준으로 정렬 == 가치/무게 == x[1]//x[0]

def myfunction(x):
    # x의 kg당 가치를 기준으로 정렬해라
    return x[1] // x[0]

arr.sort(key=myfunction , reverse=True)
arr.sort(key=lambda x:x[1] // x[0], reverse=True)
print(arr)
