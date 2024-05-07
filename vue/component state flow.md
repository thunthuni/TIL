
# props
: 부모 컴포넌트로부터 자식 컴포넌트로 데이터를 전달하는데 사용되는 속성
## passing props
: 부모는 자식에게 데이터를 pass props 
- 자식은 자신에게 일어난 일을 부모에게 emit event
## 특징
- 부모 속성이 업데이트되면 자식으로 전달 됨 
    - 하지만 자식 컴포넌트 내부에서 props를 변경 불가능
> One-Way Data Flow: 모든 props는 자식 속성과 부모 속성 사이에 하향성 단방향 바인딩을 형성
- why one-way?
    - 하위 컴포넌트가 실수로 상위 컴포넌트의 상태를 변경하여 애베서의 데이터 흐름을 이해하기 어렵게 만드는 것을 방지 
    - => 데이터 흐름의 **일관성/단일화**

## 과정
### props 선언
:부모 컴포넌트에서 내려 보낸 props를 사용하기 위해서는 자식 컴포넌테에서 명시적인 props 선언 필요

- Parent.vue
```html
<template>
    <div>
        <ParentChild my-msg="message" />
    </div>
</template>
```
- my-msg: props 이름
- "message": props 값

- ParentChild.vue

```html
<script setup>
defineProps
<script/>
```

- `defineProps()`: 에 작성하는 인자의 데이터 타입에 따라 선언 방식이 나뉨
#### 선언 방식 두가지
1. 문자열 배열을 사용한 선언
2. 객체를 사용한 선언
    > 더 권장하는 방식은 두번째
- 각 객체 속성의 키가 전달받은 props이름이 되며, 객체 속성의 값은 값이 될 데이터의 타입에 해당하는 생성자 함수여야 함
    
    ```html
    <template>
        <div>
            <p>{{ myMsg }}</p>
        </div>
    </template>
    ```
    - 1번 방식
    ```html
    <script setup>
    // 내려받은 props 를 선언 해줘야됨
    // 배열의 문자열 요소로 props 선언
    // 문자열 요소의 이름: 전달된 props 의 이름
    defineProps(['myMsg'])
    </script>

    <style scoped>
    </style>
    ```
    - 2번 방식
    ```html
    <script setup>
    // 내려받은 props 를 선언 해줘야됨

    const props = defineProps({
        myMsg: String
    })

    console.log(props) // {myMsg: 'message'}
    console.log(props.myMsg) // 'message'
    </script>

    <style scoped>

    </style>
    ```
## 세부사항
### 1. Props Name Casing
- 자식 컴포넌트로 전달시 -> **"kebab-case"**
```html
<ParentChild my-msg="message" />
```
- 선언 및 템플릿 참조 시 -> **"camelCase"**
```html
defineProps({
    myMsg:String
})
```
```html
<p> {{ myMsg }} </p>
```
### 2. Static props & Dynamic props
- v-bind 를 사용하여 동적으로 할당된 props 사용 가능


## 다른 디렉티브와 함께 사용
- v-for 와 함께 사용하여 반복되는 요소를 props로 전달하기
- ParentItem 컴포넌트 생성 및 parent 하위 컴포넌트로 등록


# Component Events
## `$emit()`
: 자식 컴포넌트가 이벤트를 발생시켜 부모 컴포넌트로 데이터를 전달하는 역할의 메서드 
- $ : vue 인스턴스의 내부 변수들을 가리킴
- 구조: `$emit(event, ...args)`
    - event: 커스텀 이벤트 이름
    - args: 추가인자
## 이벤트 발신 및 수신 
- $emit을 사용하여 템플릿 표현식에서 직접 사용자 정의 이벤트를 발신
```html
<button @click="$emit('someEvent')"> 클릭 </button>
```
- 후에 부모는 v-on 을 사용하여 수신
```html
<ParentComp @some-event="someCallback" />
```

### emit 이벤트 선언
- `defineEmits()` 를 사용하여 발신할 이벤트를 선언

### 이벤트 인자 전달 활용



## emit 이벤트 실습

## 참고 
### 왜 객체 선언 문법을 권장?
- 컴포넌트를 가독성이 좋게 문서화
- props 에 대한 유효성 검사로써 활용 가능
