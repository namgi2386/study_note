import sys
sys.stdin = open('z1.txt' , 'r')
sys.stdout = open('o1.txt', 'a')
A,B = map(int,input().split())
print(A+B)