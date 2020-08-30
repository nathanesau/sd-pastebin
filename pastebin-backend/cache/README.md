# Cache

running postgres docker for cache:

```bash
docker run -p 6379:6379 --name pastebin-redis -d redis
```