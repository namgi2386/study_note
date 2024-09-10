# 🚧그래프 기본 + 탐색🚧

## 🛴목차

[1. 그래프 기본](#그래프-기본)  
[2. DFS](#DFS)  
[3. BFS](#BFS)  
[4. Union-Find (disjoint set)](#union-find-disjoint-set)  

## 🦽그래프 기본
### 🦼 그래프 유형
+ 무향 그래프
+ 유향 그래프
+ 가중치 그래프
+ 사이클 없는 방향 그래프 (DAG)
### 🦼 그래프 표현
+ `인접 행렬`
  + 연결되지않음을 저장할 수 있다.
  + 무향그래프일때 대칭형태
  > 장점 : 연결여부를 한번에 탐색가능  
  > 단점 : 메모리 낭비발생
+ `인접 리스트`
  + 연결된 정보만을 저장
  + 코딩테스트 전용
    + 실무에서는 연결리스트사용 (삽입삭제속도good)
  > 장점 : 메모리 효율적 사용가능  
  > 단점 : 연결정보 확인이 어렵다
+ `간선의 배열`

## 🛺DFS
> 끝까지 들어갔을 때! 그때 result가 도출 된다면 DFS  
> 마지막 선택지로 돌아가기때문에 스택(재귀)을 사용한다.
#### 🚜
## 🛵BFS
#### 🚲

<div style="border:solid grey ; color:coral; ">

## 🚁Union-Find (disjoint set)
#### 🛫 `disjoint set` 
> 두개의 그래프구조에 있어서 연결 여부를 쉽게 판단하기위해 사용  
> `대표자`를 사용한다.

> ### 상호배타 집합 연산  
> + Make-Set(x) : 초기설정  
> + Union(x,y) : 같은 그룹으로 묶기  
> + Find-Set(b) : 사장 나오라그래!  
#### 🛫
#### 🛫
</div>

![image](https://noticon-static.tammolo.com/dgggcrkxq/image/upload/v1664728291/noticon/lwsssszilfkkkzdl4u1h.gif)