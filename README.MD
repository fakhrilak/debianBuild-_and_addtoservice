# INSTALL
python3 setup.py install

# CREATE SYSTEMED
    1. nano /etc/systemd/system/fakhrilak.service
    2. chomod 640 /etc/systemd/system/fakhrilak.service
    3. systemctl status fakhrilak
    4. systemctl start fakhrilak
    5. systemctl stop fakhrilak

# [FAKHRILAK.SERVICE]
[Unit]
Description=How-To Geek Service Example

Wants=network.target
After=syslog.target network-online.target

[Service]
Type=simple
ExecStart=fakhrilak start
Restart=on-failure
RestartSec=10
KillMode=process

[Install]
WantedBy=multi-user.target

