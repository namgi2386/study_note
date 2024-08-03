# T = int(input())
# for tc in range(1,T+1):
#     n ,m= map(int , input().split() )



a = '12a3'
b= a.isdecimal()
print(b)
a = 'aba287asnsod2735fh237nf32623sdfh26'
li =[]
for x in a:
    if x.isdecimal():
        li.append(x)
    else:
        li.append(" ")
print(li)
b = "".join(li)

print(b)
c =b.split()
print(c)

