import sys
sys.stdin = open('z1.txt','r')

T = int(input())

total_list = [list(map(int , input().split() )) for _ in range(6)]
atotal = list(zip(total_list))
print(total_list)