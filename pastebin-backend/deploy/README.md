# master servers

## environment variables

environment variables should be set manually in environment (for security reasons). This can be done in ``~/.bashrc``. Following variables should be set:

```bash
POSTGRES_PASS=yourpass
SQLALCHEMY_DATABASE_URI=postgresql://postgres:yourpass@yourip/postgres
REDIS_HOST=yourip
REDIS_PASS=yourpass
CELERY_BROKER_URL=yourip
CELERY_RESULT_BACKEND=yourip
SPACES_URL=https://digitalspaces.nyc3.digitaloceanspaces.com
SPACES_KEY=yourkey
SPACES_SECRET=yoursecret
```

## docker containers

redis, postgres and api should be running on master server.

redis has a 100M memory limit. If limit is exceeded, some data will be lost. Due to low site traffic this is unlikely to happen.

Critical data which should not be lost should be stored in DB instead. Currently, just hit counts are stored in redis.

Redis data is backed up by a service so data which fits inside the cache should not be lost. Backups are done regularly (every 30 seconds).

## services

backup_redis should be running on master server.

# slave servers

## environment variables

environment variables should be set manually in environment (for security reasons). This can be done in ``~/.bashrc``. Following variables should be set:

```bash
POSTGRES_PASS=yourpass
SQLALCHEMY_DATABASE_URI=postgresql://postgres:yourpass@yourip/postgres
REDIS_HOST=yourip
REDIS_PASS=yourpass
CELERY_BROKER_URL=yourip
CELERY_RESULT_BACKEND=yourip
SPACES_URL=https://digitalspaces.nyc3.digitaloceanspaces.com
SPACES_KEY=yourkey
SPACES_SECRET=yoursecret
```

## docker containers

api docker container should be running on slave server (use master redis and postgres).

## services

no services needed.
