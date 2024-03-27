# ORM(object-relational-mapping)

: 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술

## QuerySet API

: orm에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는데 사용하는 도구

```
python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 저장, 조회, 수정, 삭제하는 것
```

### 구문

- Article.objects.all()

### Query:

- 데이터베이스에 특정한 데이터를 보여 달라는 요청
- 파이썬 --ORM--> QuerySet

### QuerySet:

- django orm을 통해 만들어진 자료형
- 데이터베이스에서 전달 받은 객체 목록
  - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용가능

### Django shell

```
$ python manage.py shell_plus
```

### 데이터 객체를 만드는 3가지 방법

### 1.
