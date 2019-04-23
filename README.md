# 09_m2m

```c
09_m2m /
    09_m2m/
    	templates/
    		base.html
    	settings.py
    	urls.py
    	wsgi.py
    accounts/
    	migrations/
    	templates/
    		accounts/
    			froms.html
    			user_detail.html
    			user_followers.html
    			user_followings.html
    			user_list.html
    	admin.py
    	apps.py
    	forms.py
    	models.py
    	tests.py
    	urls.py
    	views.py
    movies/
    	fixtures/
    		genre.json
    		movie.json
    	migrations/
    	templates/
    		movies/
    			list.html
    			movie_detail.html
    	admin.py
    	apps.py
    	forms.py
    	models.py
    	tests.py
    	urls.py
    	views.py
    db.sqlite3
    manage.py
```

# Django_Project

### Technical Lead

- Web backend (Django framework, sqlite3, Python)
- Web frontend (HTML5, CSS3, Bootstrap4)
- Versioning : Git 협업 플로우

### Project Lead

- 개발 프로세스 : 
- 문서화 : Markdown 활용

### People Management

- 정기적 자체 컨퍼런스 운영





## url 접속 주소

### 페이지 VIEW 구현 URL ```GET 방식```

#### 관리자 페이지

###### /admin/



#### 계정 관련 페이지

##### 1. 유저 목록

###### /accounts/

##### 2. 유저 상세보기

###### /accounts/{user_pk}/

##### 3. 팔로우 목록보기

###### /accounts/{user_pk}/followers/

##### 4. 팔로우 목록보기

###### /accounts/{user_pk}/followings/

##### 5. 회원가입

###### /accounts/signup/

##### 6. 로그인

###### /accounts/login/



#### 영화 페이지

##### 1. 영화 목록

###### /movies/

##### 2. 영화 상세보기

###### /movies/{movie_pk}/





### 페이지 기능 구현 URL ```POST 방식```

#### 계정 관련 기능

##### 1. 팔로우 하기

###### /{user_pk}/follow/

##### 2. 로그인 하기

###### /accounts/login/

##### 3. 로그아웃 하기

###### /accounts/logout/



#### 영화 페이지 기능

##### 1. 평점 추가

###### /movies/{movie_pk}/scores/new/

##### 2. 평점 삭제

###### /movies/{movie_pk}/scores/{score_id}/delete/

