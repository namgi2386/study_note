hax_list =['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def ok_im_fine_gwaenchana(dec):
    bin =""
    for i in range(4):
        if dec & (1<<i):
            bin = '1' + bin
        else:
            bin = '0' + bin
    return bin


for tc in range(1,int(input())+1 ):
    n,str1 = input().split()
    n = int(n)
    result =""
    # re_li =[]
    for i in range(n):
        str_x = hax_list.index(str1[i])
        result += ok_im_fine_gwaenchana(str_x)
        # re_li.append(ok_im_fine_gwaenchana(str_x))
    print(f'#{tc} {result}')
    # print(f'#{tc} {"".join(re_li)}')

