# Cache

running postgres docker for cache:

```bash
docker run -p 6379:6379 --name pastebin-redis -v /root/dumps:/data -d redis redis-server --requirepass yourpass
```

to connect to image with python:

```python
import redis
r = redis.StrictRedis(host="134.122.41.28", port=6379, db=0, password='yourpass')
```

to connect to redis-cli inside docker image:

```bash
# make a data dump
docker exec -it pastebin-redis redis-cli -a yourpass --rdb /data/dump.rdb

# view keys
docker exec -it pastebin-redis /bin/bash
redis-cli -a yourpass 
KEYS *
```
