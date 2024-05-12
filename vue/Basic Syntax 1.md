# Template Syntax 
: DOM 을 기본 구성 요소 인스턴스의 데이터에 선언적으로 바인딩할 수 있는 HTML 기반 템플릿 구문을 사용
    - 바인딩: Vue instance 와 DOM 을 연결 
## 종류
### 1. Text Interpolation(보간)
```html
<p> {{message}} </p>

```
- 데이터 바인딩의 가장 기본적인 형태
- 이중 중괄호 구문을 사용
- 콧수염 구문은 해당 구성 요소 인스턴스의 msg속성 값으로 대체 
- 반응형 속성일시, msg 속성이 변경 될 때마다 업데이트 됨

### 2. Raw HTML 
- bc 콧수염 구문은 데이터를 일반 텍스트로 해석, 실제 HTML 을 출력하려면 `v-html`을 사용해야 함
```html
<div v-html="rawHtml"></div>
<script> 
    const rawHtml = ref('<span style="color:red">This should be red.</span>')
```
### 3. Attribute Bindings
- 콧수염 구문은 HTML 속성 내에서 사용할 수 없기 땜시롱 `v-bind`를 사용
- HTML 의 id 속성 값을 vue의 dynamicId 속성과 동기화 되도록 함
- 바인딩 값이 null 이나 undefined인 경우 렌더링 요소에서 제거됨
```html
<div v-bind:id="dynamicId"></div>
<script>
    const dynamicId = ref('my-id')
```
### 4. JavaScript Expressions
- Vue는 모든 데이터 바인딩 내에서 자바스크립트 표현식의 모든 기능 지원
- Vue 템프릿에서 자바스크립트 표현식을 사용할 수 있는 위치 
    - 1. 콧수염 구문 내부
    - 2. 모든 directive의 속성 값("v-"로 시작하는 특수 속성)
> 주의사항: 각 바인딩에는 하나의 단일 표현식만 포함 될 수 있음
 
## Directive
: 'v-' 접두사가 있는 특수 속성
- directive 의 속성 값은 단일 javascript 표현식이어야 함 
    - except (v-for, v-on)
- 표현식 값이 변경될 때 DOM 에 반응적으로 업데이트를 적용
```html
<p v-if="seen"> Hi There </p>
```
### 전체 구문
![Alt text](images\directive_structure.png)
- #### Arguments
    - 일부 directive 는 directive 뒤에 콜론으로 표시되는 인자 사용 가능
- #### Modifiers
    - '.' 로 표시되는 특수 접미사 -> directive 가 특별한 방식으로 바인딩되어야 함을 나타냄
- Built-in Directives
    - v-text
    - v-show
    - v-if
    - v-for

# Dynamically data binding
## v-bind
: 하나 이상의 속성 또는 컴포넌트 데이터를 표현식에 동적으로 바인딩 
- 사용처: 
    - 1. Attribute Bindings
    - 2. Class and Style Bindings


## Attribute Bindings 
-  예시 
```html
    <img v-bind:src="imageSrc" alt="#">
    <a v-bind:href="myUrl">이동!!</a>
    <!-- v-bind의 생략 구문(약어) -->
    <img :src="imageSrc" alt="#">
    <a :href="myUrl">이동!!</a>
    <p :[dynamicattr]="dynamicValue">......</p>
```
## Class and Style Bindings
- class 와 style은 모두 html 속성임 -> v-bind를 사용하여 동적으로 문자열 값을 할당할 수 있음
- ## 사용 가능한 경우 
    - ### Binding HTML Classes
        - 
