# Box model
## 구성요소 
![Alt text](box_model.png)
- 방향: top, right, left, bottom
    - 가끔 right -> start, left -> end
## box-sizing 속성
- border 포함
    - box-siging: border-box
- content만
    - box-sizing: content-box
## 박스 타입
### Normal Flow
![Alt text](normal_flow.png)
### block 타입 특징
- 항상 새로운 행으로 나뉨
- width 와 height 속성을 사용하여 너비와 높이를 지정 가능
- 기본적으로 width속성을 지정하지 X 박스는 inline 방향으로 사용 가능한 공간 모두 차지
- 대표적 block 타입: h1~6, p, div

### inline 타입 특징
- 새로운 행으로 나뉘지 X
- **width 와 height 속성 사용X**
- 수직 방향:
    - padding, margins, borders가 적용되지만 다른 요소를 밀어낼 수 X
- 수평 방향: 
    - padding, margins, borders가 적용되어 다른 요소 밀어낼 수 O
- 대표적 inline 타입 태그
    - `a`, `img`, `span`, `input`

## 속성에 따른 수평 정렬
![Alt text](horizontal_sort.png)
- 정렬을 할 때 margin/text 를 이용할 수 있는데, 둘의 관점이 매우 다르다. 
    - margin 은 공간의 관점
    - text 는 text의 관점
- 정렬을 할 때 개발자 도구를 이용하여 차지하고 있는 공간을 체크하여 이동하기 충분한지 먼저 파악해야 한다

# 기타 display 속성
1. inline- block
2. none
## inline-block 
- width와 height속성 사용 가능
- padding, margin, border로 인해 다른 요소가 밀려남
- 줄바꿈을 원하지 않으면서 너비와 높이를 적용하고 싶은 경우
## none
- 요소를 화면에 표시하지 않고, 공간조차 부여X

# shorthand속성 = 
- 4방향의 속성을 각각 지정하지 않고 한번에지정할 수 있는 속성
## 'border'
border-width, border-style, border-color 를 한번에 설정하기 위한 속성
## 'margin & padding'
#### Example 
- 4개 : 상/우/하/좌
- 3개 : 상/좌우/ 하
- 2개 : 상하/ 좌우
- 1개 : 4방향 모두 동일하게 적용

# CSS Position 
겹치는 방향이 있을 경우 Z 축을 이용하여 나타나는 순서를 설정할 수 있음
```
일반적인 상황에서는 z-index를 사용할 수 없음. position 을 설정했을 때만!
```
## 유형
1. static
    - `normal flow`를 따라감
2. relative
    - `normal flow`를 따름 -> 원래 자리를 유지
    - 이동기준점: 원래 위치 기준
3. absolute
    - normal flow를 따라가지 않음
    - 자신의 원래 공간이 없어짐
    - 이동기준점: static이 아닌 조상요소
        - 주로 가장 가까운 relative 부모 요소
    - 모두 static이면 `body`를 기준으로
4. fixed
    - normal flow를 따르지 X
    - 이동기준: 화면(viewport)
5. sticky
    - normal flow를 따름
    - 화면을 벗어나면 fixed처럼 특정 위치에 고정이 된다. 
```
fixed Vs. sticky
normal flow 를 따르는지?
```
# Z-index
- z- index의 값이 더 큰것이 우선순위가 높아짐
    - -> 더 큰 값을 가진 요소가 작은 값의 요소를 덮음

# flexbox
: 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식
## main axis
## cross axis
## flex contatiner
- 부모에게 flex를 선언한다
## flex item

- content: 여러줄
- items: 한 줄
- 

# 목적에 따른 속성 분류
- 배치: flex direction  flex wrap
- 공간: justify content align content
- 정렬: 

## flex-gro (여백분리)
- 남는 행 여백을 비율에 따란 각 flex item 에 분배
- <-> flex-shrink

## flex-basis
- flex item의 초기 크기 값을 지정

## flex direction 
![!\[Alt text\](image.png)](flex_direction.png)
## flex wrap
![Alt text](flex_wrap.png)
## justify-content
![Alt text](justify_align.png)
- space- around: 자식의 좌우 너비를 일치하게 한다 
- space - evenly: 모든 공백의 너비가 일치한다

![Alt text](align_content.png)

- 단위가 있으면 basis 없으면 shrink 

- https://flexboxfroggy.com/#ko
- css bento

