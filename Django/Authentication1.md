# 쿠키 냠냠
: 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- 클라이언트 측에서 저장되는 작은 데이터 파일이며, 사용자 인증, 추적, 상태 유지 등에 사용되는 데이터 저장 방식
## 목적
1. 세션관리
2. 개인화
3. 트래킹

```
쿠키와 세션의 목적:
서버와 클라이언트 간의 '상태'를 유지
```
## 세션
: 서버 측에서 생성되어 클라이언트와 서버 간의 상태를 유지
- 상태 정보를 저장하는 데이터 저장 방식 
- 쿠키에 세션 데이터를 저장하여 매 요청시마다 세션 데이터를 함께 보냄 
- ### 작동 원리 
    1. 클라이언트 로그인 -> 서버가 session 데이터 생성 후 저장
    2. 생성된 session 데이터에 인증 할 수 있는 session id 를 발급
    3. 발급한 session id를 클라이언트에게 응답
    4. 클라이언트는 응답 받은 session id를 쿠키에 저장
    5. 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키를 서버에 전달
    6. 쿠키는 요청 때마다 서버에 함께 전송 되므로 서버에서 session id를 확인해 로그인 되어있다는 것을 알도록 함
  
## 수명에 따른 쿠키 종류
### 1. Session cookie
: 현재 세션이 종료되면 삭제됨
- 브라우저 종료와 함께 세션이 삭제됨
### 2. Persistent cookies
: expires속성에 지정된 날짜 or max-age속성에 지정된 기간이 지나면 삭제됨
### 세션 in django
- session 의 정보는 db의 `django_session`테이블에 저장됨

## django authentication system
: 사용자 인증과 관련된 기능을 모아 놓은 시스템
### 1. 사전 준비
- 두 번째 app accounts 생성 및 settings.py에 등록
- url 분리

```
authentification 과 관련된 경로나 키워드들은 장고 내에서 accounts라는 이름으로 사용하고 있기 때문에 app의 이름을 accounts로 사용하는 것을 권장한다
```

### 2. Custom User Model 로 대체하기
- why do we have to replace user class?
  - 별도의 설정 없이 사용할 수 있어 간편하지만, 개발자가 직접 수정할 수 없는 문제가 존재

#### 1단계
: AbstractUser 클래스를 상속받는 커스텀 User클래스 작성
```python 
# accounts/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # custom 할 사항들
    pass
```
#### 2단계
```python
# settings.py 
AUTH_USER_MODEL = 'accounts.User'
```
#### 3단계
```python 
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import User

admin.site.register(User, UserAdmin)
```
### summary
- 'Auth_User_Model': Django프로젝트의 User을 나타내는 데 사용하는 모델을 지정
```
프로젝트 중간에 Auth_User_Model을 변경할 수 없음
```
## login
session을 create 하는 과정
### `AuthenticationForm()`
: 로그인 인증에 사용할 데이터를 입력 받는 built-in form
- 로그인 할때는 save 가 아니라 장고에 내장 된 login 함수를 호출해서 세션 데이터를 생성한 후에 저장 
### 로그인 로직
- create랑 다른 점
    ```python
    form = AuthenticationForm(request, request.POST)
    ```
    ```python
    if form.is_valid():
        auth_login(request, form.get_user())
    ```
- `login(request, user)`
  - AuthenticationForm을 통해 인증된 사용자를 로그인 하는 함수 
- `get_user()`
  - AuthenticationForm의 인스턴스 메서드
  - 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환
### 코드의 흐름 
#### urls.py 
```python 
app_name = 'accounts'
urlplatterns = [
  path('login/', views.login, name='login'),
]
```
#### views.py
```python 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def login(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      auth_login(request, form.get_user())
      return redirect('articles:index')
  else:
    form = AuthenticationForm()
  context = {
    'form' : form, 
  }
  return render(request, 'accounts:login', context)
```
## logout
: 현재 요청에 대한 Session Data를 DB에서 삭제 
- 클라이언트의 쿠키에서도 session id 를 삭제
### accounts/urls.py
```python 
app_name = 'accounts'
urlpatterns = [
  path('logout/', views.logout, name = 'logout'),
]
```
### accounts/views.py
```python 
from django.contrib.auth import logout as auth_logout

def logout(request):
  auth_logout(request)
  return redirect('articles:index')

```