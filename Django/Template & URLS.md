#### HTML의 컨텐츠를 변수 값에 따라 바꾸고 싶다면!!!
- views의 함수 안에 context로 딕셔너리 설정하고 
- render함수의 3번째 인자로 추가해줌 
```python
def index(request):
  context = {
    'name' : 'Jane',
  }
  return render(request, 'articles/index.html', context)
```
- 그리고 html 에서 context 안에 있는 변수를 키값을 넣어서 사용 
```
<h1>Hello, {{name}} </h1>
```
# Django Template Language(DTL)
: template 에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템 

## syntax
### 1. {{Variable}}
- render 함수의 세번째 인자로 딕셔너리 데이터를 사용 
- 딕셔너리 key 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
- dot('.')를 사용하여 변수 속성에 접근할 수 있음

### 2. Filter
```
{{variable|filter}}
{{name|truncatewords:30}}
```
### 3. Tags
```
{% tag %}
{% if %} {% endif %}
```
- 반복 또는 논리를 수행하여 제어 흐름을 만듦
- 일부 태그는 시작과 종료 태그가 필요 

### 4. comments
- DTL에서의 주석
```
{% comment %}
....
{% endcomment %}
```
- HTML에서 주석 처리를할 때 잘 확인


## 템플릿 상속
: 1. 페이지의 공통요소를 포함하고 2. 하위 템플릿이 재정의 할 수 있는 공간

### extends tag
- 자식 템플릿이 부모 템플릿을 확장한다 
```
{% extends 'path'%}
```
### block tag
- 하위 템플릿에서 재정의 할 수 있는 블록을 정의 

```
{%block name%} {%endblock name%}
```
## HTML Form
### 데이터를 보내고 가져오기
- 꼭 input값은 html의 form tag 안에 작성해야만 서버에 전송이 된다 

## 'action' & 'method' 
: form 의 핵심 속성 2가지
- 데이터를 어디로 어떤 방식으로 요청할지
### action 
- 입력 데이터가 전송될 url을 지정
- 데이터가 전달되는 목적지 
```
action = "" 
이렇게 비워둔다면 !!현재주소!!로 data를 전송한다 
```

### method (데이터 전달)
- GET : url 노출
  - 로그인할 때는 사용할 수 없음
```
method = "" 
비어있다면 기본 값은 (GET)
```
- POST : 로그인
  - header 에 담겨져서 전달된다 
---

### 'input' element
: 사용자의 데이터를 입력 받을 수 있는 요소
 
### 'name' attribute
: 입력한 데이터에 붙이는 이름 
- input에 name 속성을 적지 않는 다면 저장할 곳이 없어서 서버에 보내지 못함
## Query String Parameters
![Alt text](url_structure.png)
- 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 서버를 보내는 방법

## HTTP reqiest 객체 
- form 데이터를 가져오는 방법
```
request.GET.get('message')
```

## 과정 구현

- BASE_DIR : manage.py 의 부모폴더
- DIRS: app 폴더 외부에서도 html파일을 찾을 수 있도록 설정
1. setting에서 
  'DIRS' : [BASE_DIR / 'templates]
2. manage.py와 동일한 경로에 templates 디렉토리 생성
2. template 안에 base.html 생성
3. 기본 html 구조 body에 블럭 추가 
    - 파일이 생성되는 위치와 오타가 없는지 항상 체크하기

4. urls 에서 from articles import views
5. views에서 함수 만들기
6. 앱에서 templates\articles\index.html 생성
7.  views에서 html에서 사용할 변수 생성하고 render함수 세번째 인자 추가해주기 
8. Html 에서 변수 이용하기 
    - 태그를 이용해서 반복/ 조건 문 가능하지만
    - template에서는 과도한 로직 X

```
{}
```