# App과 URL

- include()
: 프로젝트 내부 앱들의 url을 참조할 수 있도록 매핑하는 함수

# Model
: DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능
## Model 클래스
```python
class Article(models.Model):
    title = models.CharField(max_length = 10)
    content = models.TextField()
```
- 어떤 타입의 데이터를 가지게 될지 결정하는 것 : field
1. 필드 이름
2. 필드 데이터 타입
3. (opt)필드의 제약조건

### 제약조건
: 데이터가 올바르게 저장되고 관리되도록 하기 위한 규칙

## Migrations
: model 클래스의 변경사항을 DB에 최종 반영하는 방법
- model class ---makemigrations--> migration파일 -->migrate ---> DB최종 파일
### 핵심 명령어 
- model class를 기반으로 최종 설계도 작성
```
$ python manage.py makemigrations
```
- 최종 설계도를 DB에 전달하여 반영
```
$ python manage.py migrate
```

### 이미 생성된 테이블에 필드 추가하기
```python
class Article(models.Model):
    title = models.CharField(max_length = 10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
- 필드를 추가할 때 필드의 **기본 값** 설정이 필요 

### migrate frield
- CharField()
  - max_length 가 필수 인자
- TextField()
  - : 글자의 수가 많을 때 사용
- DateTimeField의 선택인자
  - auto_new
  - auto_new_add

- 관리자 계정 생성하기
```
python manage.py createuperuser
```

