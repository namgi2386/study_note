# codes = ['ACE',]
# for st in codes[0]:
#     print(st)
#     ascii_num = ord(st)
#     print(ascii_num)
#     temp_num = (ascii_num-7) 
#     print(temp_num)
#     ascii_dec = chr(temp_num)
#     print(ascii_dec)

# print(ord('A'))
# print(ord('Z'))


codes = ['ACE',]
hea_eng = {
    'A' : 'T', 'B' : 'U', 'C' : 'V', 'D' : 'W', 'E' : 'X', 'F' : 'Y', 'G' : 'Z',
    'H' : 'A', 'I' : 'B', 'J' : 'C', 'K' : 'D', 'L' : 'E', 'M' : 'F', 'N' : 'G',
    'O' : 'H', 'P' : 'I', 'Q' : 'J', 'R' : 'K', 'S' : 'L', 'T' : 'M', 'U' : 'N',
    'V' : 'O', 'W' : 'P', 'X' : 'Q', 'Y' : 'R', 'Z' : 'S'
}
result =""
for st in codes[0]:
    result += hea_eng[st]
print(result)


codes = ['ACE',]
result =""
for st in codes[0]:
    temp_num = ord(st) - 65
    num = ( temp_num - 7) % 26 + 65
    result += chr(num)
print(result)
