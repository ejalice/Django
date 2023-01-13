# Django Test
## Custom User Model
### admin
url: http://127.0.0.1:8000/admin/

### 회원가입
url: http://127.0.0.1:8000/api/v1/register/

post에 입력 ->
{   
"email": "(이메일 입력)",   
"password": "(비밀번호 입력)"   
}   
결과 화면 -> 생성된 user model, token 등 확인 가능.

### 로그인
url: http://127.0.0.1:8000/api/v1/auth/

post: 
{   
"email": "(이메일 입력)",   
"password": "(비밀번호 입력)"   
}  
결과 화면 -> 생성된 user model, token 등 확인 가능.
