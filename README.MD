# INSTALL
python3 setup.py install

# CREATE SYSTEMED
nano /etc/systemd/system/fakhrilak.service
chomod 640 /etc/systemd/system/fakhrilak.service
systemctl status fakhrilak
systemctl start fakhrilak
systemctl stop fakhrilak
