# Many to one relationships 
## comment(N) - article(1)
: 0개 이상의 댓글은 1개의 게시글에 작성될 수 있다

### `ForeignKey()`
: N:1 관계 설정 모델 필드
### 댓글 모델 정의
```python 
#articles/models.py
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

- `NoReverseMatch` 오류는 url 태그를 확인할것
- 