## 1- default bridge network

<!-- ```bash
docker network ls
docker network inspect bridge
docker run -d --name my-nginx -p 8080:80 nginx
docker ps
docker inspect my-nginx
docker network inspect bridge
docker stop my-nginx
docker rm my-nginx
``` -->

```bash
docker network ls
docker network inspect bridge

docker run -d  -p 8081:8080 --name myapp1 nagabhushanamn/myapp
docker ps
curl http://localhost:8081/api/info

docker run -d  -p 8082:8080 --name myapp2 nagabhushanamn/myapp
docker ps
curl http://localhost:8082/api/info

ip addr show
bridge link

docker exec -it myapp1 sh
ip addr
ping networkchuck.com
ip route
curl http://172.17.0.2:8080/api/info
curl http://172.17.0.3:8080/api/info

curl http://myapp1:8080/api/info
curl http://myapp2:8080/api/info
exit

docker rm -f myapp1 myapp2
```

## 1- user-defined bridge network

```bash

docker network create my-bridge-net
docker network ls
docker network inspect my-bridge-net

docker run -d -p 8081:8080 --name myapp1 --network my-bridge-net nagabhushanamn/myapp
docker run -d -p 8082:8080 --name myapp2 --network my-bridge-net nagabhushanamn/myapp
docker ps

curl localhost:8081/api/info
curl localhost:8082/api/info

docker exec -it myapp1 sh

curl http://myapp1:8080/api/info
curl http://myapp2:8080/api/info

exit

docker rm -f myapp1 myapp2
docker network rm my-bridge-net

```

docker compose

```bash
docker-compose up -d
docker-compose ps

curl localhost:8081/api/info
curl localhost:8082/api/info

docker-compose down

```

## 3- host network

```bash
docker run -d --name myapp1 --network host nagabhushanamn/myapp
docker ps
curl localhost:8080/api/info
docker rm -f myapp1
```

## 4- none network

```bash
docker run -d --name myapp1 --network none nagabhushanamn/myapp
docker ps
docker inspect myapp1
docker exec -it myapp1 ip addr
docker rm -f myapp1
```

## 5- ipvlan network

```bash
ip addr
docker network create -d ipvlan \
  --subnet 10.1.1.0/24 \
  --gateway 10.1.1.1 \
  -o parent=eth0 \
  my-ipvlan-net \
  -o ipvlan_mode=l2
docker network ls
docker network inspect my-ipvlan-net
docker run -d --name myapp1 --network my-ipvlan-net nagabhushanamn/myapp
docker ps
docker inspect myapp1

docker exec -it myapp1 sh
ip addr
curl http://localhost:8080/api/info
exit

docker rm -f myapp1
docker network rm my-ipvlan-net

```

## 6- macvlan network

```bash

docker network create -d macvlan \
  --subnet 10.1.1.0/24 \
  --gateway 10.1.1.1 \
  -o parent=eth0 \
  my-ipvlan-net

docker network ls
docker network inspect my-ipvlan-net

docker run -d --name myapp1 --network my-ipvlan-net nagabhushanamn/myapp
docker ps
docker inspect myapp1

docker exec -it myapp1 sh


```

## 7- overlay network

```bash

(host 1) ip addr
(host 1) sudo ethtool -K ens33 tx-checksum-ip-generic off

(host 2) ip addr
(host 2) sudo ethtool -K ens33 tx-checksum-ip-generic off

(host 1) docker swarm init
(host 2) docker swarm join ...
(host 1) docker network create -d overlay --attachable my-overlay-net
(host 1) docker network ls

(host 1) docker run -d --name myapp --network my-overlay-net nagabhushanamn/myapp
(host 2) docker network ls
(host 2) docker run -dit --name myapp-v2 --network my-overlay-net nagabhushanamn/myapp
(host 2) docker network ls
(host 2) docker exec -it myapp-v2 sh

curl myapp:8080/api/info
```
