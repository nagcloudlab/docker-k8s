## Docker Networking Types

1- default bridge network
2- user-defined bridge network
3- host network
4- none network
5- ipvlan network
6- macvlan network
7- overlay network

## 1- default bridge network

```bash

docker build -t nhttpd .
docker image ls

docker run -d --name s1 nhttpd
docker inspect s1
ip addr show
docker network ls
docker inspect bridge

docker run -d --name s2 nhttpd

docker ps

docker inspect s1
docker inspect s2
docker inspect bridge

# From Host
curl http://172.17.0.2
curl http://172.17.0.3

# From Container
docker exec -it s1 bash
curl http://172.17.0.3 # s2

```

## 2- user-defined bridge network

```bash

docker network create backend --subnet 10.0.0.0/24
docker network ls
docker network inspect backend
docker network connect backend s1
docker network connect backend s2
docker network inspect backend

docker container inspect s1

docker network disconnect bridge s1
docker network disconnect bridge s2

docker exec -it s1 bash
nslookup s1
nslookup s2
nslookup <container-id>

curl s1
curl s2

traceroute s1
traceroute s2

```

```bash
docker network create frontend --subnet 10.0.1.0/24
docker network inspect frontend
docker network disconnect backend s1
docker network connect frontend s1
docker exec -it s1 bash
```

create gateway/router for backend network to communicate with frontend network

```bash
docker run -d --name gw --network backend nhttpd
docker network connect frontend gw

docker inspect gw

docker exec -it gw bash

```

```bash
docker build . -t nhttpd
docker network create backend --subnet 10.0.0.0/24
docker network create frontend --subnet 10.0.1.0/24

docker run --name s1 --network backend --cap-add=NET_ADMIN -d nhttpd
docker run --name s2 --network frontend --cap-add=NET_ADMIN -d nhttpd


docker inspect s1
docker inspect s2
docker inspect gw

//add it on s2
docker exec -it s2 bash
ip route add 10.0.0.0/24 via 10.0.1.3
exit
docker exec -it s1 bash
//add it on s1
ip route add 10.0.1.0/24 via 10.0.0.3
```

docker inspect s1
docker exec -it s2 bash
