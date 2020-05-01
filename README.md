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

### 실행

* 버전확인

```sh
$ python app.py -v
$ python app.py --version
```

```sh
$ export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES

$ python app.py --procs [프로세스 수]
$ python app.py -p [프로세스 수]
```