# HTML
: 웹 페이지의 의미와 구조를 정의하는 언어  
- Hypertext: 웹 페이지를 다른 페이지로 연결하는 링크 
- Markup Language: 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어 

## HTML element 
- opening tag <p>
- closing tag </p>
```
닫는 태그가 없는 것도 존재함
```
## attributes (class=" ")
### rules
- 속성은 요소 이름과 속성 사이에 `공백`이 있어야 함
- 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분
- 속성 값은 열고 닫는 따옴표를 감싸야 함

### function
- 추가적인 기능, 내용
- css에서 해당 요소를 선택하기 위한 값으로 활용

## Text structure
: html 주요 목적 중 하나 -> 텍스트 구조와 의미 제공
### Examples
- Heading & Paragraphs
  - h1~h6 , paragraph
  - <h1> 안뇽!!
  - <h2> 안뇽!
  - <p> 안뇽..
- Lists
  - li : list
  - ol : ordered list
    1. 하나
    2. 둘
    3. 셋
  - ul : unordered list 
    - 배
    - 고
    - 파
  ```python
  <body>
    <ol>
      <li> 마라탕
      <li> 탕수육
    </ol>
  <body>
  ```
- Emphasis & Importance
  - em: <em>기울이기</em>
  - strong: <strong>thick</strong>
  
