# HTTP

: 네크워크 상에서 데이터를 주고 받기위한 약속

## request methods

: 데이터에 어떤 요청을 원하는지를 나태내는 것

### 'Get'

: 특정 리소스를 조회

### 'POST'

: 특정 리소스에 변경(생성, 수정, 삭제)를 요구하는 요청

### CSRF

: 사이트간 요청 위조

### 팁

- 조회/ DB와 상관없는 것 : get
- 생성 수정 삭제 : post

- html 을 보여줄 필요가 있으면 render
- 이미 정의가 된 것을 그대로 사용가능하고 싶다면 redirect: 재요청
  - import render 옆에 redirect 같이 해주기
  - 재요청은 항상 GET
- html에서는 , 를 사용하지 않음
- 파이썬에서는 , 사용