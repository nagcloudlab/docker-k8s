# demo-1

```bash

docker pull nginx:latest
docker images | docker image ls
docker run -d -p 8080:80 --name webserver nginx:latest
docker ps | docker container ls
```

curl http://localhost:8080

# demo-2

```bash

git clone https://github.com/nagcloudlab/docker-k8s
cd docker-k8s/transfer-service
cat Dockerfile
docker build -t transfer-service:latest .
docker tag transfer-service:latest nagabhushanamn/transfer-service:latest
docker push nagabhushanamn/transfer-service:latest
docker image ls
docker run -d -p 8080:8080 --name transfer-service transfer-service:latest

curl http://localhost:8080
```
