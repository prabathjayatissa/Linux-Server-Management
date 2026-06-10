
# Linux (RedHat / CentOS / RHEL) Server Command Cheat Sheet

## Disk & Storage
```bash
df -h
du -sh *
lsblk
mount
fdisk -l
blkid
```

## Memory & CPU
```bash
free -h
top
htop
nproc
lscpu
```

## System Performance
```bash
uptime
vmstat 1
iostat -xz 1
sar -u 1
```

## Network & Ports
```bash
ip a
ip r
ss -tulnp
netstat -tulnp
ping google.com
curl -I http://localhost:8080
```

## Firewall (firewalld - IMPORTANT in RHEL/CentOS)
```bash
systemctl status firewalld
systemctl start firewalld
systemctl enable firewalld

firewall-cmd --state
firewall-cmd --list-all
firewall-cmd --permanent --add-port=443/tcp
firewall-cmd --reload
```

## SELinux (Very important in RHEL/CentOS)
```bash
getenforce
sestatus
setenforce 0   # temporary permissive
setenforce 1   # enforcing
```

## Services (systemd)
```bash
systemctl status nginx
systemctl start nginx
systemctl stop nginx
systemctl restart nginx
systemctl enable nginx
systemctl list-units --type=service
```

## Logs & Debugging
```bash
journalctl -xe
journalctl -u nginx
tail -f /var/log/messages
tail -f /var/log/secure
dmesg | tail
```

## Users & Permissions
```bash
whoami
id
who
chmod 755 file.sh
chown user:user file.txt
```

## Docker
```bash
docker ps
docker ps -a
docker logs container_name
docker exec -it container_name bash
docker images
docker network ls
docker-compose up -d
docker-compose down
```

## Security & Ports Audit
```bash
ss -tulnp
lsof -i -P -n
nmap localhost
```

## Package Management (VERY DIFFERENT from Ubuntu)
```bash
yum update
yum install package_name
yum remove package_name
yum list installed
```

# OR (newer systems using dnf)
```bash
dnf update
dnf install package_name
dnf remove package_name
dnf list installed
```

## System Info
```bash
cat /etc/redhat-release
hostnamectl
```

