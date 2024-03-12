## 용어
- client: 서비스를 요청하는 주체
  - 웹 사용자의 인터넷이 연결된 장치, 웹 브라우저
- server: 클라이언트의 요청에 응답하는 주체 
  - 웹 페이지, 앱을 저장하는 컴퓨터
- Frontend: 
  - 사용자 인터페이스 구성
  - 사용자가 애플리케이션과 상호작용할 수 있도록 하는 역할
- Backend:
  - 서버 측에서 동작
  - 클라이언트의 요청에 대한 처리와 데이터베이스와의 상호작용 담당

## Web Framework
  : 웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구
  - 개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공

# DJANGO
: 파이썬 기반의 대표적인(검증된) 웹 프레임워크
### :)
- 다양성
- 확장성
  - 대량의 데이터에 빠르고 유연하게 확장할 수 있음
- 보안
- 커뮤니티 지원
  - 개발자를 위한 지원, 문서 및 업데이트를 제공하는 활성화 된 커뮤니티

## 가상환경
: python 애플리케이션과 그에 따른 패키지들을 **격리**하여 **관리**할 수 있는 독립적인 실행 환경

## django프로젝트 생성 전 
1. 가상 환경 venv생성
  ```
  $ python -m venv venv
  ```
- python -m venv : 명령어
- 뒤에 venv: 가상환경 이름
- venv 안에 있는 파일은 절대로 건들지 말것

2. 가상 환경 활성화
- 내가 가상환경(파일)에 들어가는 것이 아니라 환경을 on off 하는 것이다 

```
ON 
$ source venv/Scripts/activate
```
3. 패키지 목록 확인
```
$ pip list
```
- 패키지들간에 복잡한 의존성이 존재하므로 관리를 잘해야한다
- 동료에게 가상환경에서 진행한 프로젝트를 공유할 때 git hub를 통해서 할 수 없다 
  - 설치한 package list를 같이 공유해야 한다


4. 의존성 패키지 목록 생성
#### 의존성 패키지
: 한 소프트웨어 패키지가 다른 패키지의 기능이나 코드를 사용하기 때문에 그 패키지가 존재해야만 제대로 작동하는 관계
```
$ pip freeze > requirements.txt
```
- 다른 이름으로도 txt가 만들어지기는 하지만 `requirements`라는 이름을 꼭 써줘야 한다
```
requiremennts 통해서 설치하기
$ pip install -r requirements.txt
```
## 프로젝트 생성 전 루틴
1. 가상환경 생성
2. 가상환경 활성화
```
맥북
scripts 대신 Bin
```
3. Django 설치
```
맥북
pip install django == 4.2
```
4. 의존성 파일 생성
  - 패키지 설치시마다 진행
5. .git ignore 파일 생성
6. git 저장소 생성
7. Django 프로젝트 생성

## 프로젝트 생성 
1. 프로젝트 생성
```
django-admin startproject firstpjt.
```
- . 을 끝에 붙으면 현재 위치에서 프로젝트를 생성한다는 뜻

2. 서버 실행
```
python manage.py runserver
```
3. 서버 확인
- https://127.0.0.1:8000/

# Django Design Pattern
: 소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책
- 해결책을 최대한 일반화 하기 위해서 애플리케이션의 구조를 공통적으로 사용하는 것을 지향
## MVC 디자인 패턴
: Model, View, Controller
- 애플리케이션을 구조화하는 대표적인 패턴
- 데이터 & 사용자 인터페이스 & 비즈니스 로직 을 분리
## MTV 디자인 패턴
: Model, Templete, View
- MVC 와 동일하나 명칭만 다름

# Project & App
- Django project
: 애플리케이션의 집합
- DB 설정, URL 연결, 전체 앱 설정 등을 처리
- Django application
: 독립적으로 작동하는 기능 단위 모듈

```
앱을 사용하기 위한 순서
1. 앱 생성
2. 앱 등록
* 순서를 꼭 지켜야 한다 
```
### 명령어 
1. 앱 생성
```
$ python manage.py startapp articles
```
- 앱의 이름(articles)은 복수형으로 지정해라

2. 앱 등록
```python
INSTALLED_APPS = [
    'articles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
- pjt 파일안에 있는 settings.py 에서 앱을 등록하는데 이미 등록되어있는 앱 앞에 등록하는 것을 권장한다 

### 프로젝트 구조
- 수정할 파일
  - `settings.py`
    - 프로젝트의 모든 설정을 관리
  - `urls.py`
    - 요청 들어오는 URL 에 따라 이에 해당하는 적절한 views를 연결
- 수정할 일 없는 파일
  - `__init__.py`
    - 해당 폴더를 패키지로 인식하도록 설정하는 파일
  - `asgi.py`
    - 비동기식 웹 서버와의 연결 관련 설정
  - `wsgi.py`
    - 웹 서버와의 연결 관련 설정
  - `manage.py`
    - Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티

### 앱 구조
- 수정할 파일
  - `admin.py`
    - 관리자용 페이지 설정
  - `models.py`
    - DB 와 관련된 Model 을 정의
    - MTV 패턴의 M
  - `views.py`
    - HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환
    - MTV 패턴의 V
```
MTV 의 T 는 기본 파일로 생성되지 않고 사용자가 만들어야 한다
왜? 장고는 백엔드 기본 프레임워크이기 때문
```

# 요청과 응답
- urls 에서 요청 분류 
- view에서 실행 
  - DB에서 데이터 가지고 오고 templates에서 템플릿 가지고 와서 데이터와 templates를 결합해서 완성된 html을 응답한다 
1. URLs
