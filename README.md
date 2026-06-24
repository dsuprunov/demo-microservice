# README.md

## Local Two-Service Test

The local Docker Compose setup starts two services:

* `demo-microservice-a` sends messages to `demo-microservice-b`
* `demo-microservice-b` sends messages to `demo-microservice-a`

Console 1:

```bash
docker compose -f src/docker-compose.yaml up --build demo-microservice-a
```

Console 2:

```bash
docker compose -f src/docker-compose.yaml up --build demo-microservice-b
```

## Manual Ping

```bash
curl -i -X GET http://localhost:8001/ping \
  -H "Content-Type: application/json" \
  -d '{
    "message_id": "msg-001",
    "service_id": "demo-microservice-manual",
    "instance_id": "instance-01",
    "payload": "hello"
  }'; echo
```

## Docker 

```bash
docker build \
  -t dsuprunov/demo-microservice:0.1.0 \
  -t dsuprunov/demo-microservice:latest \
  src

docker image ls dsuprunov/demo-microservice

docker login

docker push dsuprunov/demo-microservice:0.1.0
docker push dsuprunov/demo-microservice:latest

docker buildx imagetools inspect dsuprunov/demo-microservice:0.1.0
docker buildx imagetools inspect dsuprunov/demo-microservice:latest
```

## Kubernetes

```bash
kubectl apply -f manifests/demo-microservice-a.yaml
kubectl apply -f manifests/demo-microservice-b.yaml

kubectl get deployment,pod,service -n demo-microservice-a
kubectl get deployment,pod,service -n demo-microservice-b

kubectl logs -n demo-microservice-a -l app=demo-microservice-a -f
kubectl logs -n demo-microservice-b -l app=demo-microservice-b -f
```
