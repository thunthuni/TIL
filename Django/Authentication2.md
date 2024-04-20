# 회원가입 sign up 
## `UserCreationForm()`
: 회원 가입시 사용자 입력 데이터를 받는 built-in ModelForm
- 바로 사용할 수 없는 이유는 usermodel을 custom 한 것이기 때문에
- user 커스텀하면 장고 기본 유저를 하는 것이 아님
- modle = User(장고 기본 유저) 에서 model이 바뀌고 유저 커스텀을 새롭게 등록해야 함

## AttributeError 
- 커스텀한 유저 모델을 사용하면서 UserCreationForm을 그대로 사용할 때 생기는 오류 

- AttributeError at /accounts/signup/ 
- Manager isn't available; 'auth.User' has been swapped for 'accounts.User'
  - 유저모델 커스텀 -> 기존 기본 유저모델로 변경하면 됨
  - UserCreationForm
  - UserChangeForm
    - 두 폼 모두 class Meta: model = User가 작성된 Form
- ### 오류 해결하기 at forms.py
   
  
```python 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
  class Meta(UserCreationForm.Meta):
    model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
  class Meta(UserChangeForm.Meta):
    model = get_user_model()
```
- Meta 로 부터 상속받아서 모델만 바꾸고 나머지는 유지

- #### `get_user_model()`

  : '현재 프로젝트에서 활성화된 사용자 모델'을 반환하는 함수

- #### why not user_model()?

  : get_user_model()을 사용해 user모델을 참조하면 커스텀user 모델을 자동으로 반환해주기 때문
> 중요: 장고에서 필수적으로 User클래스를 직접 참조하는 대신 get_user_model()사용해서 참조해야 하기를 지향

## 회원가입 로직
```python 
from .forms import CustomUserCreationForm

def signup(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('articles:index')
  else:
    form = CustomUserCreationForm()
  context = {
    'form': form,
  }
  return render(request, 'accounts/signup.html', context)
```
### 회원가입 이후 바로 로그인 s
```python
if form.is_valid():
  user = form.save()
  auth_login(request, user)
  return redirect('articles:index')
```
# 회원 탈퇴
- AnonymousUser: 로그인 되지 않은 상태
- 로그인한 user 정보는 request.user에 들어있음
- anonymousUser 가 기본적으로 request.user 에 들어있어서 로그인 하면 자동적으로 삭제 됨

```python
def delete(request):
    if request = 'POST':
        request.user.delete()
        return reidrect('articles:index')
```

# 회원정보 수정
## `UserChangeForm()`
- 회원정보 수정 시 사용자 입력 데이터를 받는 built-in ModelForm
- User 모델의 모든 정보들까지 모두 출력되어 수정이 가능이 가능하기 때문에 일반 사용자들이 접근해서는 안되는 정보는 출력하지 않도록 해야 한다
  - => CustomUserChangeForm 을 사용해서 필드를 다시 조정해야함
  ```python 
  # accounts/forms.py
  class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
      model = get_user_model()
      fields = ('first_name', 'last_name', 'email',)

### 로직
```python
def update(request):
  if request.method == 'POST':
    form = CustomUserChangeForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      return redirect('articles:index')
  else:
    form = CustomUserChangeForm(instance=request.user)
  context = {
    'form': form,
  }
  return render(request, 'accounts/update.html', context)
```

# 비밀번호 변경 
: 인증된 사용자의 Session 데이터를 Update 하는 과정 
## `PasswordChangeForm()`
: 비밀번호 변경 시 사용자 입력 데이터를 받는 built-in Form
```python
def change_password(request, user_pk):
  if request.method == 'POST': 
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      form.save()
      return redirect('articles:index')
  else:
    form = PasswordChangeForm(request.user)
  context = {
    'form': form,
  }
  return render(request, 'accounts/change_password.html', context)
```
### `upadate_session_auth_hash(request, user)`
: 암호 변경 시 세션 무효화를 막아주는 함수
- 암호가 변경되면 새로운 password의 Session data로 기존 session을 자동으로 갱신
```python
from django.contrib.auth import update_session_auth_hash

def change_password(request, user_pk):
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)
      return redirect('articles:index')
  else:
    form = PasswordChangeForm(request.user)
  context = {
    'form' : form,
  }
  return render(request, 'accounts/change_password.html', context)
```
## `is_authenticated` / `login_required`
- is_authenticated
```python
if request.user.is_authenticated
```
```html
{% if request.user.is_authenticated %}
```
- login_required
: 인증된 사용자에 대해서만 view 함수 실행시키는 데코레이터 
- 비인증이라면 /account/login/ 주소로 redirect
```python
from django.contrib.auth.decorators import login_required

@login_required
def logout(request):
  pass
```