# 🎇문자열🎇

---

### ✨문자의 표현✨ in computer
+ 1bit는 `0`or`1`
+ 6bit는 `2^6` == 64가지 표현 가능
+ 영어 대소문자는 52개 ➡ 6bit로 표현가능

### 🐅ASCII&emsp;for incording
+ 0번~ 31번 , 127번 : 제어문자
+ 32번~126번 : 출력가능한 아스키 문자
+ `16진수`도 알아야됨.
+ 확장 아스키에서는 8bit로 사용
+ 1byte == 8bit : 주소부여되는 최소단위  

### 🐪유니코드&emsp;다국어 처리 표준
+ usc-2 usc-4 ?
+ UTF-8 : ?
+ UTF-16 : 윈도우,자바
+ UTF-32 : unix 
+ 파이참에서도 아래에 UTF-8 : 인코딩방식 적혀있음

### 🦝문자열의 종류
> 문자열 저장할 때 어디서부터 어디까지가 문자인지를 알려줘야댐
> 
> java에서는 문자열의 길이를 함께 저장함
> 
> c언어에서는 문자열 끝에 `\0`를 자동저장해줌

---
## ✨실습✨
#### 1. python 에서의 문자저장
```python
import sys

a = ''
b = 'a'
c = 'ab'
d = 'abc'

print(sys.getsizeof(a))# 빈칸이라도 str타입이니까 49byte
print(sys.getsizeof(b)) # 50
print(sys.getsizeof(c)) # 51
print(sys.getsizeof(d)) # 52
```
#### 2. list(input()) , input() 비교
```python
s1 = list(input())
s2 = input()

print(s1) # abc입력시, ['a','b','c']
print(s2) # abc입력시, abc
```
#### 3. list와 string의 인덱스 그리고 수정
```python
s1 = list(input())
s2 = input()
print(s1[0]) # abc입력시, a
print(s2[0]) # abc입력시, a

s1[0] = 'E' # 리스트라서 가능
s2[0] = 'E' # string이라서 불가능
```
#### 4. strlen() 함수 만들기
> 생략
#### 5. 문자열 뒤집기 
```python
n=5
arr = list('algorithm')
for i in range(n//2):
    arr[i] , arr[n-1-i] = arr[n-1-i] , arr[i]
```
```python
print(arr[::-1])
```
```python
s ='abracadabra'
# 뒤집기
s_reverse =""
for i in range(len(s)):
    s_reverse += s[len(s) - 1 -i]
print(s)
print(s_reverse)
```
#### 6. `==` , `is` 비교 in python
> `==` : 값이 같음?
> 
> `is`  : 주소가 같음? (주소=참조위치) (나중에배울개념)
```python
s1 = 'abc'
s2 = 'abc'
l1 = [1,2,3]
l2 = [1,2,3]
print(s1 == s2) # True
print(l1 == l2) # True
print(s1 is s2) # True
print(l1 is l2) # False
```

#### 7. 문자열 숫자를 정수로 변환하기 
> `int()` 함수 만들기
```python
def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x) -ord('0')
    return i
```
> `str()` 함수 만들기
```python
#우선 생략
```
### 🎲python 개꿀 기능🎲
```python
for i in range(5):
    if a != 3:
        break
else : # for문이 중단된적없다면! 실행됨
    print("succese")
```