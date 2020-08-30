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
curl http://localhost:5000/api/v1/paste?shortlink=1XSatxf

# /api/v1/paste
curl -H "Content-Type: application/json" -XPOST --data '{"expiration_length_in_minutes": "43200", "paste_contents": "Hello World!"}' http://localhost:5000/api/v1/paste

# /api/v1/stats
curl -H "Content-Type: application/json" "http://127.0.0.1:5000/api/v1/stats/hits?period=2020-08&shortlink=6rOuJIk"
```

Running API:

```bash
set FLASK_APP=pastebin-api.py
flask run
```