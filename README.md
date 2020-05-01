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
      "HOST": "",
      "PORT": 6379
    },
    "mysql": {
      "USER":"",
      "PASSWORD":"",
      "HOST":"",
      "DB":""
    }
  }
}
```