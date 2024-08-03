import sys
sys.stdin = open('z_d.txt','r')

last_date_monthly_str = '1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31'
ldms_list = last_date_monthly_str.split(", ")
date_str_list = [0]*len(ldms_list)
for idx in range(len(ldms_list)):
    idx_cut = ldms_list[idx].split("/")
    date_str_list[idx] = int(idx_cut[1])



last_date_list = [31,28,31,30,31,30,31,31,30,31,30,31]

T = int(input())
for tc in range(1,T+1):
    result = 0
    m1,d1 ,m2 , d2 = map(int,input().split())
    for idx_m in range(m1,m2):
        result += last_date_list[idx_m-1]
    result -= (d1 -1)
    result += d2
    
    print(f'#{tc} {result}')
