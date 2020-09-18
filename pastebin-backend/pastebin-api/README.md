# pastebin-api

API reference:

| Endpoint | Request | Arguments | Response |
| -------- | --------| --------- | -------- |
| ``/api/v1/paste`` | ``POST`` | ``{"expiration_length_in_minutes": "43200", "paste_contents": "Hello World!"}`` | ``{"shortlink": "foobar"}`` |
| ``/api/v1/paste?shortlink=foobar`` | ``GET`` | N/A | ``{"paste_contents": "Hello World", "created_at": "YYYY-MM-DD HH:MM:SS", "expires_at": "YYYY-MM-DD HH:MM:SS"}`` | 
| ``/api/v1/stats/hits?period=2020-08&shortlink=1XSatxf`` | ``GET`` | N/A | ``{"hits": "2"}`` |

API tests:

```bash
# /api/v1/paste?shortlink=foobar
curl http://api.pastebin.io:5000/api/v1/paste?shortlink=3kyFdv2

# /api/v1/paste
curl -H "Content-Type: application/json" -XPOST --data '{"expiration_length_in_minutes": "43200", "paste_contents": "Hello World!"}' http://api.pastebin.io:5000/api/v1/paste

# /api/v1/stats
curl -H "Content-Type: application/json" "http://api.pastebin.io:5000/api/v1/stats/hits?period=2020-09&shortlink=uaCyzSj"
```

API https tests (letsencrypt used for certificate and key):

```bash
# /api/v1/paste?shortlink=foobar
curl https://api.pastebin.io/pastebin-api/api/v1/paste?shortlink=uaCyzSj

# /api/v1/paste
curl -H "Content-Type: application/json" -XPOST --data '{"expiration_length_in_minutes": "43200", "paste_contents": "Hello World!"}' https://api.pastebin.io/pastebin-api/api/v1/paste

# /api/v1/stats
curl -H "Content-Type: application/json" "https://api.pastebin.io/pastebin-api/api/v1/stats/hits?period=2020-09&shortlink=uaCyzSj"
```

Running API:

```bash
set FLASK_APP=pastebin-api.py
flask run
```

Docker Instructions:

```bash
docker build -t pastebin-api:latest .
docker run --name pastebin-api --restart always -d -p 5000:5000 -v /root/pastes:/pastes -v /root/cache:/cache pastebin-api:latest
```
