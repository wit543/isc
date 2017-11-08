```bash
docker run --cap-add=SYS_ADMIN -ti -e "container=docker" -v /sys/fs/cgroup:/sys/fs/cgroup --name centos centos:latest /usr/sbin/init

  yum update -y && yum install -y git zsh

  yum install -y yum-utils \
    device-mapper-persistent-data \
    lvm2

  yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

  yum install -y docker-ce
```