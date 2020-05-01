# 영화 크롤러

### 설정파일 

* 환경설정

.env

```
MODE=develop
```

* 설정파일


config/config.json

```json
{
  "develop": {
    "redis": {
      "HOST": "localhost",
      "PORT": 6379
    }
  }
}
```