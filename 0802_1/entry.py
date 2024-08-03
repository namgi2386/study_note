import sys
sys.stdin = open('z_e.txt','r')



T = int(input())
for tc in range(1,T+1):
    n , m = map(int,input().split())
    time_list = [int(input()) for _ in range(n)]
    time_list.sort()
    
    back_up_time_list = time_list.copy()

    for _ in range(m-1):
        shortest_entry_idx = time_list.index(min(time_list))
        time_list[shortest_entry_idx] += back_up_time_list[shortest_entry_idx]

    print(f'#{tc} {min(time_list)}')


        




