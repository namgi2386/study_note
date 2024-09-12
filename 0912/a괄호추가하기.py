def h(a, b, oper):
    if oper == "+":
        return a + b
    elif oper == "-":
        return a - b
    elif oper == "*":
        return a * b


def g():
    m = (n - 1) // 2
    visited = []
    max_num = -1e9
    for dec in range(1 << m):  # dec번째 부분집합
        result_arr = []
        num_arr = list(range(n))
        li = []
        for i in range(m):
            if dec & (1 << i):
                if 2 * (i - 1) not in li and 2 * (i + 1) not in li:
                    num_arr.remove(2 * i)
                    num_arr.remove(2 * i + 1)
                    num_arr.remove(2 * i + 2)
                    li.append(2 * i)
        for i in num_arr:
            result_arr.append((i , arr[i]))
        if li not in visited:
            visited.append(li)
            for idx in li:
                a = arr[idx]
                oper = arr[idx + 1]
                b = arr[idx + 2]
                temp_num = h(a, b, oper)
                # print(temp_num)
                # print(result_arr)
                result_arr.append((idx, temp_num))
                # print(result_arr)
            result_arr.sort(key=lambda x:x[0])

            # print(result_arr)
            while len(result_arr) != 1:
                _,a = result_arr.pop(0)
                _,oper =result_arr.pop(0)
                _,b = result_arr.pop(0)
                result_arr.insert(0,(0,h(a,b,oper)))
            max_num = max(max_num , result_arr[0][1])
    return max_num



n = int(input())
arr = list(map(lambda x: x if x in "+-*" else int(x), input()))

print(g())
