# nginx

Nginx is for https support.

Instructions:

* copy sites-enabled files to /etc/nginx/sites-enabled (pastebin-api)
* nginx -t (check if configuration is valid)
* service nginx start (if applicable) 
* service nginx reload

Test:

```bash
# https: without -k the self-signed certificate is not trusted
curl -k https://api.pastebin.io/pastebin-api/api/v1/paste?shortlink=uaCyzSj
curl -k https://api.pastebin.io/pastebin-api/api/v1/paste?shortlink=uaCyzSj

# http
curl http://api.pastebin.io/pastebin-api/api/v1/paste?shortlink=uaCyzSj

# https mimic
curl https://cors-anywhere.herokuapp.com/http://api.pastebin.io:5000/api/v1/paste?shortlink=uaCyzSj
```