## JavaScript 실행환경 종류

1. HTML script 태그
2. js 확장자 파일
3. 브라우저 Console

# DOM (The Document Object Model)

: 웹 페이지를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공

- 문서 구조, 스타일, 내용 등을 변경할 수 있도록 함
- DOM API: 다른 프로그래밍 언어가 웹 페이지에 접근 및 조작 할 수 있도록 페이지 요소들을 객체 형태로 제공/ 메서드 또한 제공
- 특징:
  - 모든 요소, 속성, 텍스트는 하나의 객체
  - 모두 document 객체의 하위 객체로 구성
- 핵심:
  - 문서의 요소들을 객체로 제공하여 다른 프로그래밍 언어에서 접근하고 조작 할 수 있는 방법을 제공하는 API

## `document` 객체

- 웹 페이지 객체
- DOM Tree의 진입점
- 페이지를 구성하는 모든 객체 요소를 포함

## DOM 선택

- 조작순서

1. 조작 하고자 하는 요소를 선택
2. 선택된 요소의 콘텐츠 또는 속성을 조작

### 선택 메서드

- `document.querySelector()`
  - 제공한 선택자와 일치하는 element 한 개 선택
  - 제공한 CSS selector 를 만족하는 첫 번째 element 객체를 반환
    - 없다면 return null
- `document.querySelectorAll()`
  - 제공한 선택자와 일치하는 여러 element를 선택
  - 제공한 CSS selector 를 만족하는 NodeList 를 반환

## DOM 조작

### 속성 조작

- ### 클래스 속성 조작
  - 'classList' property
  - : 요소의 클래스 목록을 DOMTokenList(유사 배열) 형태로 반환
  -
- ### 일반 속성 조작
  - `Element.getAttribute()`
  - `Element.setAttribute(name, value)`
  - `Element.removeAttribute()`
