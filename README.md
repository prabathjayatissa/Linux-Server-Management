# Linux-Server-Management


# Linux (Ubuntu) Server Command Cheat Sheet

## Disk & Storage
```bash
df -h
du -sh *
lsblk
mount
fdisk -l
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

## Firewall (UFW)
```bash
ufw status
ufw allow 443/tcp
ufw allow 22/tcp
ufw enable
ufw deny 8080
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
tail -f /var/log/syslog
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

## Updates & Packages
```bash
apt update
apt upgrade
apt install package_name
dpkg -l
```

