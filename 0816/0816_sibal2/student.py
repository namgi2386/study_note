import sys
sys.stdin =open('z1.txt','r')

def last_date(c):
    date_count = 0
    if c==0:
        return 0
    for i in range(7):
        if arr[i] == 1:
            date_count += 1
            if date_count == c:
                c_date = i + 1
                return c_date

def empty_date():
    counts = 0
    for i in range(7):
        if arr[i] == 0:
            counts += 1
        else:
            return counts


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    w = sum(arr) # weekly_date

    last = n%w
    week = n//w

    if last == 0:
        week -= 1
        last = w
    result = 7*week + last_date(last) - empty_date()

    print(f'#{tc} {result}')
