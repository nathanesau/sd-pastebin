# nginx

Nginx is for https support.

Instructions:

* copy sites-enabled files to /etc/nginx/sites-enabled (pastebin-api)
* nginx -t (check if configuration is valid)
* service nginx start (if applicable) 
* service nginx reload

Test:

```bash
# https support
curl https://api.pastebin.io/pastebin-api/api/v1/paste?shortlink=uaCyzSj
curl https://api.pastebin.io/pastebin-api/api/v1/paste?shortlink=uaCyzSj
```
