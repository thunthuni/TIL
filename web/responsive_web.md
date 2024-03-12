#### 치팅 시트
https://docs.emmet.io/cheat-sheet/
### 대표 단축키
- 라인 하나 선택 : ctrl+l
- 동일 키워드 연속 선택하기: ctrl + d
- 멀티 커서: ctrl + alt + 화살표
- 멀티 커서: alt + 클릭
- 선택한 라인 끌고가기 : alt + 화살표 
- 선탁한 라인 복사: alt + shift + 화살표

# Bootstrap Grid system
: 웹 페이지의 레이아웃을 조정하는 데 사용되는 12개의 컬럼으로 구성된 시스템
- Grid system: 화면 크기에 따라 12개의 칸을 각 요소에 나누어 주는 것 

## 목적
: 반응형 디자인을 지원해 웹 페이지를 모바일, 태블릿, 데스크탑 등 다양한 기기에서 적절하게 표시할 수 있도록 도움 

## 반응형 웹 디자인
: 디바이스 종류나 화면 크기에 상관없이, 어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술 

## 기본 요소
1. container
  - column 들을 담고 있는 공간
2. column
  - 실제 컨텐츠를 포함하는 부분
3. gutter
  - 컬럼과 컬럼 사이의 여백 영역


## Gutters
: grid system에서 column 사이에 여백 영역
- x축은 padding, y축은 margin 으로 여백 생성

# responsive web design
: 디바이스 종류나 화면 크기에 상관없이, 어디서든 일관된 레이아웃 및 사용자 경험을 제공
```
Bootstrap grid system에서는 12개 column과 6개 breakpoints를 사용하여 반응형 웹 디자인을 구현
```
## Grid system breakpoints
: 웹 페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점
- 화면 너비에 따라 6개의 분기점 제공
  - xs, sm, md, lg, xl, xxl
  ```
  xs은 분기점이 없음
  ```
![Alt text](breakpoints.png)

#### html 복습 사이트
https://web.dev/learn/html
#### 클론 코딩 추천
인스타그램