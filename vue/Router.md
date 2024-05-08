# Routing
: 네크워크에서 경로를 선택하는 프로세스
- 웹 애플리케이션에서 다른 페이지 간의 전환과 경로를 관리하는 기술
- SPA 에서 Routing 이 없다면
    - 유저가 url 을 통한 페이지의 변화를 감지 X
    - 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 X
    - 브라우저의 뒤로 가기 기능을 사용할 수 X
    > 페이지는 1개이지만, 주소에 따라 여러 컴포넌트를 새로 렌더링하여 마치 여러 페이지를 사용하는 것처럼 보이도록 해야 함

- 공식 문서
    - https://v3.router.vuejs.org/

## 구조 변화
- RouterLink: 
    - 페이지를 다시 로드 하지 안혹 url 을 변경하여 url 생성 및 관련 로직을 처리 
    - html 의 a 태그를 렌더링
- RouterView:
    - RouterLink url 에 해당하는 컴포넌트를 표시
    - 원하는 곳에 배치하여 컴포넌트를 레이아웃에 표시 가능
- views:
    - router 와 연결되는 components
    - 기존 components폴더와 기능적으로 다른것은 없지만 분류를 위해서 구분

## 기본
1. index.js 에 라우터 관련 설정 작성
2. RouterLink 의 'to ' 속성으로 index.js 
3. RouterLink클릭 시 경로와 일치하는 컴포턴트가 routerview 에서 렌더링 됨

## Named Routes
- name 속성 값에 경로에 대한 이름을 지정
- 경로에 연결하려면 routerlink에 v-bind를 사용해 'to' props 객체로 전달

- App.vue
```html
<RouterLink :to="{ name: 'home' }"> Home </RouterLink>
```
- 장점: 하드 코딩 된 url 을 사용 X / 오타방지

## Dynamic Route Matching
: URL 의 일부를 변수로 사용하여 경로를 동적으로 매칭

## Nested Router
- 애플리케이션의 UI 는 여러 레벨 깊이로 중첩된 컴포넌트로 구성되기도 함
- 이 경우에 url 을 중첩된 컴포넌트의 구조에 따라 변경되도록 이 관계에 표현할 수 있음



## Programmatic Navigation
: RouterLink대신 javascript를 사용해 페이지를 이동하는 것
### router의 메서드 
- ### router.push()
![Alt text](images/router.push().png)
    : 다른 URL로 이동하는 메서드 
    - 새 항목을 history stack 에 push 하므로 사용자가 브라우저 뒤로 가기 버튼을 클릭하면 이전 url로 이동할 수 있음


# Navigation Guard
: vue router 를 통해 url 에 접근할 때 다른 URL로 redirect 를 하거나 취소하여 내비게이션을 보호 
- 라우트 전환 전/후 자동으로 실행되는 Hook

## 종류
1. Globally
2. Per-route
3. In-component

## 1. Globally Guard
: 애플리케이션 전역에서 동작하는 가드
- 작성위치: index.js
### - `router.beforeEach()` = 'Global before Guards'
: 다른 url로 이동하기 직전에 실행되는 함수
```html 
<script>
router.beforeEach((to, from ) => {
    ....
    return false 또는 return { name: 'About'}
})
</script>
```
- 모든 가드는 2개의 인자를 받음
    - to: 이동 할 url 정보가 담긴 Route객체
    - from: 현재 url 정보가 담긴 Route객체
- 선택적으로 다음 값 중 하나를 반환
    - false:
        - 현재 내비게이션을 취소
        - 브라우저 URL 이 변경된 경우 'from' 경로의 URL로 재설정
    - Route Location: 
        - router.push()를 호출하는 것처럼 경로 위치를 전달하여 다른 위치로 redirect return 이 없다면 자동으로 'to' URL Route 객체로 이동
