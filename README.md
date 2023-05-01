# LectureProject-django

simple jwt를 이용해 access, refresh 토큰 발행

```
 token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "register successs",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )

            # # jwt 토큰 => 쿠키에 저장
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)

            return res
```
DRF 내장 함수인 TokenObtainPairSerializer은 로그인 시 JWT를 생성 및 반환한다.
#### access token = 클라이언트가 서버에 요청을 보낼 때마다 함께 전송되어, 서버가 <br> 해당 요청을 처리할 때 사용자 인증을 수행하는 데 사용된다.
#### refresh token = accesstoken을 발급해주는 토큰으로 acceess토큰으로 인증된 사용자가 지속적으로 서비스를 이용할 수 있게 해준다. <br> 사용자가 자주 로그인하는 불편함을 줄이면서도, 보안성을 높일 수 있다.
