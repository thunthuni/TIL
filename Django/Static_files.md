# static files

: 서버 측에서 변경되지 않고 고정적으로 제공되는 파일

- ex) 이미지, js, css

### 웹 서버의 기본동작:

- 특정 위치(URL)에 있는 자원을 요청 받아서 응답을 처리하고 제공
- 정적 파일을 제공하기 위한 경로가 있어야 함

## 정적파일 제공하기

#### 1. 기본 경로에서 제공하기

- app폴더/static/

### STATIC_URL

: 기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL

#### 2. 추가 경로에서 제공하기

### STATICIFILES_DIRS

: 정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트

```
정적 파일을 제공하려면 요청에 응답하기 위한 url 이 필요하다
```

# media files

: 사용자가 웹에서 업로드하는 정적 파일

- ### ImageField()

  : 이미지 업로드에 사용하는 모델 필드

  ```
  pip install Pillow
  한 후에
  migration 작업

  ```

- ### MEDIA_ROOT
  : 실제 미디어 파일들이 위치하는 디렉토리의 절대 경로
- ### MEDIA_URL

  : MEDIA_ROOT 에서

- 초기 설정
  1. form tag
  - enctype 설정
  - multipart/form-data
  2. ArticleForm(request.POST, request.FILES)
