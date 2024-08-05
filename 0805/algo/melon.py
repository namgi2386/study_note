import sys
sys.stdin = open('z1.txt','r')

T = int(input())

n1 ,m1= map(int , input().split() )
n2 ,m2= map(int , input().split() )
n3 ,m3= map(int , input().split() )
n4 ,m4= map(int , input().split() )
n5 ,m5= map(int , input().split() )
n6 ,m6= map(int , input().split() )
#total_list = [list(map(int , input().split() )) for _ in range(6)]

direction_list = [n1,n2,n3,n4,n5,n6]
length_list =    [m1,m2,m3,m4,m5,m6]

a_li =[]
b_li =[]

for i in range(4):
    if direction_list[i] == direction_list[i+2]:
        anti_area = length_list[i+1]*length_list[i+2]
        break

max_a = 0
max_b = 0
for i in range(6):
    if direction_list[i] == 1 or direction_list[i] == 2:
        if direction_list[i] > max_a:
            max_a = length_list[i]
    else:
        if direction_list[i] > max_b:
            max_b = length_list[i]

maximum_area = max_a*max_b
result = maximum_area - anti_area
#print(maximum_area , anti_area)
print(result*T)
