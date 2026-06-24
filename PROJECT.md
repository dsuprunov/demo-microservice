# PROJECT.md

# Demo Microservice 0.1.0

## Goal

Build a simple Kubernetes demo application that demonstrates:

* Service to Service Communication
* Health Checks
* Structured Logging
* Failure Handling
* Replica Awareness
* Best Effort Delivery

The project is not intended for production use.

The project is intended for learning, testing, and demonstration.

---

## Services

The system contains three services:

* demo-microservice-a
* demo-microservice-b
* demo-microservice-c

All services use the same Docker image.

Behavior is controlled by configuration.

---

## Technology Stack

Use current stable versions at implementation time:

* Python
* FastAPI
* Uvicorn
* Docker
* Kubernetes

---

## Docker Image

Repository:

dsuprunov/demo-microservice

Tags:

* 0.1.0
* latest

Both tags must be published.

---

## API

Only two endpoints are allowed:

GET /healthz

GET /ping

No additional endpoints may be added without approval.

---

## Message Contract

{
"message_id": "uuid",
"service_id": "demo-microservice-a",
"instance_id": "pod-name",
"timestamp": "2026-06-24T12:34:56Z",
"payload": "msg-000001"
}

---

## Timestamp

Use:

* UTC
* ISO 8601

Example:

2026-06-24T12:34:56Z

---

## Delivery Model

Best Effort

Rules:

* Single attempt
* No retry
* No queue
* No persistence
* No backpressure

Delivery failure must not stop the service.

---

## Error Model

Errors are stored as plain strings.

Example:

{
"error": "connection timeout"
}

No error codes.

No error identifiers.

No error categories.

---

## Logging

All logs must be JSON.

Events:

* STARTUP
* DELIVERED
* FAILED
* RECEIVED
* SHUTDOWN

Every message related log must contain:

* message_id
* payload

---

## Configuration

Required environment variables:

* SERVICE_ID
* INSTANCE_ID
* PEERS
* INTERVAL
* TIMEOUT

PEERS must be a JSON array.

Example:

[
"http://demo-microservice-b:8000/ping"
]

---

## Kubernetes

INSTANCE_ID should normally come from:

metadata.name

using fieldRef.

---

## Explicitly Out Of Scope

Do not add:

* Retry
* Queue
* Database
* Redis
* Kafka
* RabbitMQ
* Prometheus
* Grafana
* OpenTelemetry
* Tracing
* Authentication
* Authorization
* Service Mesh
* Ingress
* API Gateway
* Status Endpoint
* Version Endpoint
* Debug Endpoint
