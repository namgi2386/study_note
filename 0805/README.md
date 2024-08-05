# 🦓string🐴

## 패턴매칭 알고리즘 🌲
> + 고지식한 패턴 검색 알고리즘
> + 카프 라빈 알고리즘
> + kmp 알고리즘
> + 보이어 무어 알고리즘
### #1 고지식한 알고리즘 🌼
```python
def frute(p,t):
    i = j = 0
    n = 10
    m=20
    t = 'TTTTTTATTAATA'
    p = 'TTA'
    while i<n and j<m:
        if t[i] != p[j]:
            i = i-j
            j = -1
        i = i+1
        j = j+1
    if j == m :
        return i-m # 성공
    else :
        return -1 # 실패

        
```
### #2 KMP 알고리즘 🌻

### #3 보이어 무어 알고리즘 🌷
> 이건 몰라도 됨  

> + 글짜 확인 후 찾는패턴의 끝글짜와 비교
>   + 불일치 > 그 글짜가 패턴속에 포함되는지 확인
>       + 없으면 PASS
>       + 있으면 글짜 위치에 맞추고나서 나머지 글짜 확인
>           + 맞다면 CATCH!
>           + 안맞다면 패턴의 길이만큼 JUMP
### #4 문자열 매칭 알고리즘 비교🌾
+ 문자열 패턴길이 M , 총문자열길이 N
+ 고지식한 패턴 검색 : O(mn)
+ 카프라빈 알고리즘 : 세타(n)
+ kmp 알고리즘 : 세타(n)
+ 보이어 무어 알고리즘 : 
### #5 연습문제3🌿
```python
def f(t,p): #패턴 p와 일치하는 구간의 시작인덱스리턴 , 없으면 -1 리턴
    n = len(t)
    m = len(p)
    
    for i in range(n-m+1):
        for j in range(m):
            if t[i+j] != p[j]:
                break
        else:
            return 1
    return -1

t = 'TTTTTTATTAATA'
p = 'TTA'
print(f(t,p))
```
## 문자열 암호화 🌳`참고`
+ 시저 암호
+ 단일 치환 암호
+ bit열 암호화 exclusive-or 연산 사용
+ run length encoding 알고리즘