arr =list(input())
n = len(arr)
for i in range(n//7):
    print(int("".join(arr[7*i:7*i+7]),2) , end=" ")
print()


