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

#print(arr[::-1])
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
 ![image](data:image/png;base64,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)
 