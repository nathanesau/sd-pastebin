# service instructions

```bash
cp services/upload_pastes/upload_pastes.service /lib/systemd/system/
chmod 644 /lib/systemd/system/upload_pastes.service
cp /lib/systemd/system/upload_pastes.service /etc/systemd/upload_pastes.service

# enable to start service on reboot
systemctl enable upload_pastes

# start service
systemctl start upload_pastes
```
