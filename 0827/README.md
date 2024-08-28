# 🎄트리 1🎄
> 0827
## ✨목차✨
[1. 트리](#트리-기본)  
[2. 이진트리](#이진트리)  
[3. 이진트리 순회✨](#이진트리-순회)  
[4. 이진트리의 표현](#이진트리의-표현)  
[5. 이진트리의 저장](#참고-이진트리의-저장)  
[6. 연습문제✨](#연습문제)  
[7. 이진탐색 트리 (내일예정)](#이진탐색-트리)  
[8. 힙 (내일예정)](#힙)  

---

## 🩲트리 기본🩲
+ 👑비선형구조 (순서없음)
+ 👑1:n
+ 👑계층형
+ 👑나무모양
+ 👑차수와 높이로 구성되며, 순환되지 않는다
  + 높이=깊이=level


|지금까지 배운| 자료구조 |
|---|---|
|선형 |비선형|
|스택|딕셔너리|
|큐| set|
|덱|해쉬|
|연결리스트|<span style="background-color:#FFF5b1;">그래프</span>|

<div style="width:35rem; margin:auto;">
<img src="https://hanamon.kr/wp-content/uploads/2021/07/%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%E1%84%80%E1%85%AE%E1%84%8C%E1%85%A9-%E1%84%90%E1%85%B3%E1%84%85%E1%85%B5-%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%8B%E1%85%A5.png" alt="트리기본사진">
</div>

<div><details><summary style="font-size:1.5rem; "><strong>👑노드 용어 설명👑</strong> </summary>

+ 루트노드 : 시작노드
+ 부모노드 : 부모노드
+ 형재노드 : 같은부모 자식노드들
+ 조상노드 : 직계 부모노드들
+ 서브트리 : 부모노드 끊었을 때 생성되는 트리
+ 자손노드 : 서브트리의 하위노드들
+ 리프노드 : 자식이 없는 끝지점 노드들
</details></div>

<div style="margin-left: auto; border: solid rebeccapurple; height: 2rem; width: 4rem; text-align:center;"><a href="https://hanamon.kr/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-tree-%ED%8A%B8%EB%A6%AC/">출처</a></div>

---
---

## 👕이진트리👕 
#### 👚기본이진트리
+ 트리형태 중 모든 노드에서의 자식노드가 `최대 2개` 일때, 그 트리가 이진트리
+ 최대높이가 `h` 일때 노드수 최소 `h+1` , 최대 `2^(h+1) -1` 

#### 👚포화이진트리
+ 최대높이 `h` 일때 노드수 최대 `2^(h+1) -1` 개 
#### 👚완전이진트리
+ 최대높이 `h` , 노드수 `n` 개 일때, 포화이진트리의 노드번호 `1번부터 n번까지`의 자리를 차지하고 있는 이진트리
#### 👚편향이진트리
+ 최대높이 `h` , 노드수 최소 `h+1` 개 , 한쪽방향진행


## 🩳이진트리 순회🩳
#### 👒전위 순회 `pre order`
<div style="width:25rem">
<img src="https://www.jiwon.me/content/images/size/w1000/2021/11/preorder.png" alt="전위순회">
</div>

#### 👒중위 순회 `in order`
<div style="width:25rem">
<img src="https://www.jiwon.me/content/images/size/w1000/2021/11/inorder.png" alt="중위순회">
</div>

#### 👒후위 순회 `post order`
<div style="width:25rem">
<img src="https://www.jiwon.me/content/images/size/w1000/2021/11/postorder.png" alt="후위순회">
</div>

<div style="margin-left: auto; border: solid rebeccapurple; height: 2rem; width: 5rem; text-align:center; margin-bottom: 0.5rem "><a href="https://www.jiwon.me/binary-tree-traversal/">img 출처</a></div>


## 🧥이진트리의 표현 (사용안함)🧥
> 실습코드에서는 그림과는 달리 D부모노드의 자식 노드로 F , G 노드가 위치한다.

```py
# 전위 순회 탐색 코드
def preorder(a):
    if a <= N:
        print(tree[a], end=' ')
        preorder(a*2)
        preorder(a*2 + 1)
 
N = 9
tree = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I']
print(tree)
preorder(1)

#출력 A B D H I E C F G
```

> 실습코드에서는 그림과는 달리 D부모노드의 자식 노드로 F , G 노드가 위치한다.
```py
# 중위 순회 탐색 코드
def inorder(a):
    if a <= N:
        inorder(a*2)
        print(tree[a], end=' ')
        inorder(a*2 + 1)
 
N = 9
tree = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I']
print(tree)
inorder(1)

#출력 H D I B E A F C G
```

> 실습코드에서는 그림과는 달리 D부모노드의 자식 노드로 F , G 노드가 위치한다.
```py
# 후위 순회 탐색 코드
def postorder(a):
    if a <= N:
        postorder(a*2)
        postorder(a*2 + 1)
        print(tree[a], end=' ')
 
N = 9
tree = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I']
print(tree)
postorder(1)

#출력 H I D E B F G C A
```

<div style="margin-left: auto; border: solid rebeccapurple; height: 2rem; width: 5rem; text-align:center;"><a href="https://edder773.tistory.com/46">code 출처</a></div>


## 👓[참고] 이진트리의 저장👓
> 2개의 배열을 사용하여 구현  
> 연습문제 참고

## 🧦연습문제🧦

```py
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
'''
               1
          2         3
        4       5      6
       7      8  9   10  11
     12                   13
'''

def pre_order(T):
    if T:
        print(T, end = ' ')
        pre_order(left[T])
        pre_order(right[T])
def in_order(T):
    if T:
        pre_order(left[T])
        print(T, end = ' ')
        pre_order(right[T])
def post_order(T):
    if T:
        pre_order(left[T])
        pre_order(right[T])
        print(T, end = ' ')

N = int(input())        # 1번부터 N번까지인 정점
E = N-1
arr = list(map(int, input().split()))
left = [0]*(N+1)        # 부모를 인덱스로 왼쪽자식번호 저장
right = [0]*(N+1)       #
par = [0]*(N+1)         # 자식을 인덱스로 부모 저장

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
# for i in range(0,E*2, 2):
#         p, c = arr[i], arr[i + 1]
    if left[p]==0:          # 왼쪽자식이 없으면
        left[p] = c
    else:
        right[p] = c
    par[c] = p

c = N
while par[c]!=0:        # 부모가 있으면
    c = par[c]          # 부모를 새로운 자식으로 두고
root = c                # 더이상 부모가 없으면 root
print(root)
pre_order(root)
```

## 👜이진탐색 트리👜
> 내일!

## 👟힙👟
> 내일!