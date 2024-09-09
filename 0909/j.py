def is_correct(from_li , to_li):
    if 0 in from_li and 2 in to_li:
        return True
    if 1 in from_li and 3 in to_li:
        return True
    if 2 in from_li and 0 in to_li:
        return True
    if 3 in from_li and 1 in to_li:
        return True
    return False

a =[0,1]
b =[3,4]

print(is_correct(a,b))
