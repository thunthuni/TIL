## `ManyToManyField`

- 다대다 관계에서는 종속 관계가 아니다

  - 필드를 두는 위치에 따라서 참조/역참조가 달라진다

- through: 중개 테이블로 사용할 것을 지정해주므로 add/remove 를 자유롭게 사용할 수 있음

```
patient.doctors.all()
doctor.patient_set.all()
```

## 대표 methods

- `add()`
  - 지정된 객체를 관련 객체 집합에 추가
- `remove()`
  - 관련객체 집합에서 지정된 모델 객체를 제거

## 좋아요 구현하기

- Article(M) - User(M)
- 역참조 매니저 충돌
  - 다대다 관계에서 related_name 작성
