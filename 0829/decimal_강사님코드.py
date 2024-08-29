
decimal = 149

# 비트연산으로 진수변환하기
# num&1 해당 비트가 1인지 0인지 판단하기

def dec_to_bin(dec):
    bin =""
    for i in range(7,-1,-1):
        if dec & (1<<i): # 결과값은 0 혹은 1 , 10 , 100 , 10000 등등 가능
            bin += "1"
        else:
            bin += "0"
    print(bin)

dec_to_bin(149)