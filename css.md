

# CSS

css ranking

<https://developer.microsoft.com/en-us/microsoft-edge/platform/usage/>

내가쓰고있는 브라우저 점수

https://html5test.com/

<https://caniuse.com/>



### 픽셀, %, em

---

rem 

- em의 기준은 상속의 영향으로 바뀔수 있다.

- 1rem = 16px
- 정확한 크기조절을 할 수 있다.
- r은 root를 의미



viewport 단위

- viewport 기준으로 만든 단위



속성의 우선순위

- !important :0순위 > inline(내부) > embedding > file link > browser default
- 단, 동일한 ```<head>```에 외부스타일을 정의할 경우, 나중에 적용한게 우선순위



멀티 컨트롤  - ctrl + art 혹은 art

라인복사 - art- shift 방향키





### 색상표현 단위

---

### span 태그

span태그와 div 태그는 모두 의미는 없지만 마크업을 해야 css를 적용시킬 수 있기 때문에 활용된다.

---

시맨틱태그의 필요성-- 의미!

----

nth-of-type 을 더선호

nth-child() 자식중에 2번째

nth-of-type 같은 타입 형제중 2번째






```css
.border-box{

 box-sizing: border-box;

}

```

-------------

### block

항상 새로운 라인

화면 크기 전체 가로폭

### inline

새로운라인에서 시작하지 않고 문장 중간에 들어갈 수 있음.

### inline block	

가로세로 마진값 조정가능

### none 

공간조차 사라짐





---



### relative

- position 적용전(static일때) 기준으로 움직임. 움직인 후 원래공간으로 유지

### absolute

- absolute는 집나간 자식 /relative 찾아감

- 부모가 static이면 그위의 부모 새로찾아감.
- 움직일때 붕뜨고 움직인 후에 자리 없어짐.