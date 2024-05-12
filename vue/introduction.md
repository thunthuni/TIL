## Client-side frameworks
: 크ㄹ라이언트 축에서 ui와 상호작용을 개발하기 위해 사용되는 JS 기반 프레임워크
- 필요이유:
    - 웹의 기능이 늘어나며 웹이 그저 조회용 을 넘어서 무언가를 하는 곳이 됐음
        - 복잡한 대화형 웹 사이트: 웹 애플리케이션
    - 웹에서 하는 일이 많아짐 -> 다루는 데이터양 증가
    
## Single Page Application (SPA)
: 단일 페이지로 구성된 애플리케이션

- 하나의 HTML 파일로 시작하여, 사용자가 상호작용할 때마다 페이지 전체를 새로 로드하지 않고 화면의 필요한 부분만 동적으로 갱신
- 대부분 javascript 프레임워크를 사용하여 클라이언트 측에서 UI 와 렌더링을 관리
- <-> MPA(Multi Page Application) : 여러 개의 HTML 파일이 서버로부터 각각 로드
    - 사용자가 다른 페이지로 이동할 때마다 새로운 HTML 파일이 로드

## Client-side Rendering (CSR)
: 클라이언트에서 화면을 렌더링 하는 방식
- <-> SSR: 서버에서 화면을 렌더링 하는 방식 
    - 모든 데이터가 담긴 HTML 을 서버에서 완성 후 클라이언트에게 전달
    - 하지만 CSR 이랑 완전 반대개념은 아님

### :)
1. 빠른 페이지 전환
    - 페이지가 처음 로드된 후에는 필요한 데이터만 가지고 오면 됨
        - JS는 전체 페이지를 새로 고침할 필요 없이 페이지의 일부를 다시 렌더링 할 수 있음
    - 서버로 전송되는 데이터의 양을 최소화
2. 사용자 경험
    - 새로고침이 발생하지 않아서 네이티브 앱과 유사한 사용자 경험을 제공
3. frontend와 backend의 명확한 분리

### :(
1. 느린 초기 로드 속도
    - 전체 페이지를 보기 전에 약간의 지연
        - bc JS가 다운로드, 구분 분석/실행될 때까지 페이지가 완전히 렌더링 되지 않음
2. SEO(검색 엔진 최적화) 문제
    - 페이지를 나중에 그리기 때문에 검색에 잘 노출되지 않을 수 있음
    - 검색엔진 입장에서 HTML 을 읽어서 분석해야 하는데 아직 콘텐츠가 모두 존재하지 않음


# VUE
: 사용자 인터페이스를 구축하기 위한 JavaScript 프레임워크
## 핵심 기능
1. 선언적 렌더링
    - 표준 HTML 을 확장하는 '템플릿 구문'을 사용하여 JavaScript 상태를 기반으로 화면에 출력된 HTML을 선언적으로 작성

2. 반응성
    - JavaScript 상태 변경을 추적하고, 변경사항이 발생하면 자동으로 DOM 을 업데이트

## 사용방법
1. 'CDN' 방식
```html
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
    // CDN 에서 Vue를 사용하는 경우 전역 Vue 객체를 불러오게 됨
    const {createApp} = Vue
    // 모든 Vue 애플리케이션은 createApp함수로 새 Application instance 를 생성하는 것으로 시작
    const app = createApp({})
    // HTML 요소에 Vue 애플리케이션 인스턴스를 탑재
    // 각 앱 인스턴스에 대해 mount()는 한번만 호출할 수 있음
    app.mount('#app')
```
### `ref()`
: 반응형 상태를 선언하는 함수(Declaring Reactive State)
- 반응형을 가지는 참조 변수를 만드는 것 
- ref 로 선언된 변수의 값이 변경되면, 해당 값을 사용하는 템플릿에서 자동으로 업데이트 
- 템플릿의 참조에 접근하려면 setup 함수에서 선언 및 반환 필요
    ```html
    <script> 
        const app = createApp({
            setup() {
                const message = ref('Hello vue!')
                return {
                    message
                }
            }
        })
    ```
    - createApp() 에 전달되는 객체는 Vue 컴포넌트 
        - 컴포넌트의 상태는 setup() 함수 내에서 선언되어야 하며 객체를 반환해야 함
- unwrap 시 ref 가 최상위 속성이 경우에만 가능
- ref 필요 이유: 
    - vue 는 템플릿에서 ref 를 사용하고 나중에 ref 의 값을 변경하면 자동으로 변경 사항을 감지하고 그에 따라 dom을 업데이트 함
        - : 의존성 추적 기반의 반응형 시스템 
    - vue 는 렌더링 중에 사용된 모든 ref를 추적하며, 나중에 ref 가 변경되면 이를 추적하는 구성 요소에 대해 다시 렌더링
    