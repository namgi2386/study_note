## baby gin game

---

> ## 6장 카드 속 triple or run 2개조합 가능 할 때 baby gin
>
> ### 1. tripe : 같은숫자 3개
>
> ### 2. run : 연속숫자 3개

> ### ☆예시 문제 풀이☆
>
> #### #1 444345 입력 받음
>
> #### #2 counts(카운팅 정렬)을 이용하여 각 숫자의 갯수를 counts에 저장
>
> ```py
> num = 456789
> c = [0] * 12
> for i in range(6):
>     c[ num % 10 ] += 1
>   num //= 10
> ```
>
> #### #3 만약 run일때 count에서 1씩 감소시킨 이후 triple인지 검사한다면 311100 일때는 200100 되면서 예외발생
>
> #### #4 그래서 triple 검사 후 run 검사
>
> ```py
> i =0
> tri = run = 0
> while i < 10 :
>    if c[i] >= 3:
>        c[i] -= 3
>        tri += 1
>        continue
>    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1
>        c[i] -= 1
>        c[i+1] -= 1
>        c[i+2] -= 1
>        run += 1
>        continue
>    i += 1
>
> if run + tri == 2 : print("baby gin")
> else : print("lose")
> ```

## 완전탐색 : brute-force

---

> IM 수준에서는 완전탐색 가능  
> 정확성 중요  
> 효율성은 필요한 반복문만 사용한 정도면 OK , But 필요없는 반복문이 추가되어 효율성이 떨어진다면 안됨..

-   완전 탐색을 통한 baby gin == 6개 숫자의 모든 경우의 수 각각 계산

---

## 순열

-   순열을 이용하여 baby gin 해결해보자

> nPr : n개 중 r개 택하는 경우의 수

```py
# 1234 중 3 개뽑아서 나오는 결과의 종류
for i1 in range(1,4):
    for i2 in range(1,4):
        if i2 != i1:
            for i3 in range(1,4):
                if i3 != i1 and i3 != i2:
                    print(i1,i2,i3)

# >>> (1 2 3) (1 3 2) (2 1 3) (2 3 1) (3 1 2) (3 2 1)
```

---

## 탐욕 알고리즘 : Greedy!

> ### 매 순간 최선의 선택을 하는 근시안적인 알고리즘
>
> -   최종 결과가 최적의 답은 아님
> -   생각나는대로 구현했을때 greedy

> ### 거스름돈 줄이기
>
> > 어떻게 하면 손님에게 거스름돈의로 주는 지폐와 동전의 갯수를 줄일 수 있을까?
>
> 나중에 풀어봐

-끝-
