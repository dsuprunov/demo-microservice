# Demo Microservice

## Manual Run

```bash
docker compose -f src/docker-compose.yaml up --build

curl -i -X GET http://localhost:8000/healthz ; echo

curl -i -X GET http://localhost:8000/ping \
  -H "Content-Type: application/json" \
  -d '{
    "message_id": "msg-001",
    "service_id": "demo-microservice",
    "instance_id": "instance-01",
    "timestamp": "2026-06-24T12:00:00Z",
    "payload": "hello"
  }'; echo
```
