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

## Services

The system contains two services:

* demo-microservice-a
* demo-microservice-b

All services use the same Docker image.

Behavior is controlled by configuration.

## Technology Stack

Use the following stack:

* Python 3.14
* FastAPI
* Uvicorn
* Docker
* Kubernetes

## Dependencies

Do not add dependencies without justification.

Document dependency justification in the change summary or project docs.

## Python

Format Python code according to PEP 8.

Do not add docstrings unless explicitly requested.

## Development Environment

Application runtime and Python checks must run inside Docker containers.

Do not require Python installation on the host.

Do not require Python modules installation on the host.

## Docker Image

Repository:

dsuprunov/demo-microservice

Tags:

* 0.1.0
* latest

Both tags must be published.

## API

Only two endpoints are allowed:

* `GET /healthz`
* `GET /ping`

No additional endpoints may be added without approval.

## Message Contract

```json
{
  "message_id": "uuid",
  "service_id": "demo-microservice-a",
  "instance_id": "pod-name",
  "payload": "msg-000001"
}
```

## Delivery Model

Best Effort

Rules:

* Single attempt
* No retry
* No queue
* No persistence
* No backpressure

Delivery failure must not stop the service.

## Error Model

Errors are stored as plain strings.

Example:

```json
{
  "error": "connection timeout"
}
```

No error codes.

No error identifiers.

No error categories.

## Logging

Log lines must use the current application log format:

```text
<utc_log_time>Z <level> <json_payload>
```

Example:

```text
2026-06-24T12:34:56Z INFO {"event":"STARTUP","service_id":"demo-microservice-a"}
```

The JSON payload must contain the event-specific structured fields.

Events:

* STARTUP
* DELIVERED
* FAILED
* RECEIVED
* SHUTDOWN

Every message related log must contain:

* `message_id`
* `payload`

## Configuration

Required environment variables:

* `SERVICE_ID`
* `INSTANCE_ID`
* `PEERS`
* `INTERVAL`
* `TIMEOUT`

PEERS must be a JSON array.

Example:

```json
[
  "http://demo-microservice-b:8000/ping"
]
```

## Kubernetes

The Kubernetes manifests must include these services:

* `demo-microservice-a`
* `demo-microservice-b`

Each service manifest must include:

* `Namespace`
* `Deployment`
* `Service`

Each service must have its own namespace:

* `demo-microservice-a`
* `demo-microservice-b`

Each deployment must set `INSTANCE_ID` from `metadata.name` using `fieldRef`.

Services must communicate using Kubernetes service DNS.

Use the `service.namespace` form for cross-namespace peers:

* `demo-microservice-a.demo-microservice-a`
* `demo-microservice-b.demo-microservice-b`

Kubernetes peer URLs must use these values:

* `demo-microservice-a` sends to
  `http://demo-microservice-b.demo-microservice-b:8000/ping`
* `demo-microservice-b` sends to
  `http://demo-microservice-a.demo-microservice-a:8000/ping`
