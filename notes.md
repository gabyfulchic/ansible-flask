## Setup docker
```bash
yum install yum-utils device-mapper-persistent-data lvm2 -y
yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
yum install docker-ce docker-ce-cli containerd.io -y
```
