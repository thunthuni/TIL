# event 객체
: 무언가 일어났다는 신호, 사건 
- 모든 DOM 요소는 이러한 event를 만들어 냄
> DOM 요소는 event 를 받고 받은 event 를 처리 할 수 있음

## event handler
: 이벤트가 발생했을 때 실행되는 함수 
- 사용자의 행동에 어떻게 반응할지를 JavaScript 코드로 표현한 것
### `.addEventListener()`
: 특정 이벤트를 DOM 요소가 수신할 때마다 콜백 함수를 호출
![Alt text](images\structure_of_addEventListener.png)
- 대상에 특정 event 가 발생하면, 지정한 이벤트를 받아 할 일을 등록한다
- #### addEventListener 의 인자
    - type: 수신할 이벤트 이름
        - 문자열로 작성 
    - handler : 발생한 이벤트 객체를 수신하는 콜백 함수
        - 콜백 함수는 발생한 event object 를 유일한 매개변수로 받음

## Bubbling
: 한 요소에 이벤트가 발생하면, 이 요소에 할당된 핸들러가 동작하고, 이어서 부모 요소의 핸들러가 동작하는 현상

### currentTarget 주의사항
- console.log()로 event 객체를 출력할 경우 currentTarget 키의 값은 null을 가짐
- currentTarget 은 이벤트가 처리되는 동안에만 사용할 수 있기 때문
- => current Target 이후의 속성 값들은 'target'을 참고해서 사용
## 예시
```

```

- lodash 