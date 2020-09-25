# service instructions

## backup_redis

performed every 30 seconds in the background.

backs up redis cache to ``/root/dumps`` folder.

```bash
# cp required files
cp services/backup_redis/backup_redis.service /lib/systemd/system/
cp /lib/systemd/system/backup_redis.service /etc/systemd/backup_redis.service
chmod 644 /lib/systemd/system/backup_redis.service

# enable to start service on reboot
systemctl enable backup_redis

# start service
systemctl start backup_redis
```
