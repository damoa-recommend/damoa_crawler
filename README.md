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

* 

```sh
+[__NSPlaceholderDate initialize] may have been in progress in another thread when fork() was called.
+[__NSPlaceholderDate initialize] may have been in progress in another thread when fork() was called. We cannot safely call it or ignore it in the fork() child process. Crashing instead. Set a breakpoint on objc_initializeAfterForkError to debug.
```

해당 에러가 발생한다면 다음과 같이 환경변수 설정

```sh
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
```