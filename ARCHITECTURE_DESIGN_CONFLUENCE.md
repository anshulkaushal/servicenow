# Event-Driven Integration Architecture Design - Confluence Format

> **Note:** This document is formatted for Confluence. Copy sections as needed into your Confluence pages.

---

h1. Event-Driven Integration Architecture Design
h2. ServiceNow Integration with JIRA, GitHub, Ansible, and Azure Red Hat OpenShift

{panel:title=Document Information|borderStyle=solid|borderColor=#0052CC|titleBGColor=#E3FCEF|bgColor=#FFFFFF}
* *Document Type:* Architecture Design Document
* *Project:* ServiceNow Event-Driven Integration
* *Version:* 1.0
* *Date:* [Current Date]
* *Status:* Draft - Pending Approval
{panel}

---

h1. Executive Summary

{panel:title=Overview|borderStyle=solid|borderColor=#0052CC|titleBGColor=#E3FCEF|bgColor=#FFFFFF}
This document describes the architecture for integrating JIRA, GitHub, Ansible Automation Platform, and Azure Red Hat OpenShift with ServiceNow using an event-driven architecture. The solution enables automatic creation of change requests and incident tickets in ServiceNow based on events from these tools, with reliable event processing, acknowledgment mechanisms, and resilience to ServiceNow outages.
{panel}

h2. Key Objectives
* Automate ticket/change request creation in ServiceNow based on events from integrated tools
* Provide reliable event processing with queue-based resilience
* Enable bidirectional communication with acknowledgment mechanisms
* Support high-volume event processing with scalability
* Ensure event delivery even during ServiceNow outages

---

h1. Architecture Overview

h2. High-Level Architecture

{code:language=text|title=Architecture Diagram|collapse=false}
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│    JIRA     │     │   GitHub    │     │   Ansible   │     │  OpenShift  │
│             │     │             │     │             │     │             │
└──────┬──────┘     └──────┬──────┘     └──────┬──────┘     └──────┬──────┘
       │                   │                   │                   │
       │  Webhooks/Events  │  Webhooks/Events  │  Webhooks/Events  │  Webhooks/Events
       │                   │                   │                   │
       └───────────────────┴───────────────────┴───────────────────┴───────────┐
                                                                                 │
                                                                                 ▼
                                                          ┌──────────────────────────────┐
                                                          │   Event Management Layer     │
                                                          │  (Apache Kafka / RabbitMQ)    │
                                                          │                              │
                                                          │  • Event Ingestion           │
                                                          │  • Event Normalization       │
                                                          │  • Event Enrichment         │
                                                          │  • Event Queue Management    │
                                                          └──────────────┬───────────────┘
                                                                         │
                                                                         ▼
                                                          ┌──────────────────────────────┐
                                                          │   Event Processing Engine    │
                                                          │  (Custom Middleware/Service) │
                                                          │                              │
                                                          │  • Event Filtering          │
                                                          │  • Event Routing             │
                                                          │  • Transformation Logic     │
                                                          │  • Retry Logic              │
                                                          └──────────────┬───────────────┘
                                                                         │
                                                                         ▼
                                                          ┌──────────────────────────────┐
                                                          │      ServiceNow API          │
                                                          │                              │
                                                          │  • Create Change Request     │
                                                          │  • Create Incident           │
                                                          │  • Update Records            │
                                                          │  • Send Acknowledgment       │
                                                          └──────────────┬───────────────┘
                                                                         │
                                                                         │ Acknowledgment
                                                                         │ (Change/Incident #)
                                                                         │
                                                                         ▼
                                                          ┌──────────────────────────────┐
                                                          │   Acknowledgment Handler     │
                                                          │                              │
                                                          │  • Receive ACK from SN      │
                                                          │  • Update Source Systems     │
                                                          │  • Log Acknowledgment        │
                                                          └──────────────────────────────┘
{code}

h2. Architecture Principles

# *Event-Driven:* Asynchronous, decoupled event processing
# *Resilient:* Queue-based architecture ensures no event loss
# *Scalable:* Horizontal scaling capability for high-volume events
# *Reliable:* Retry mechanisms and dead letter queue handling
# *Observable:* Comprehensive logging and monitoring
# *Secure:* End-to-end encryption and authentication

---

h1. Component Architecture

h2. Event Sources Layer

h3. JIRA Integration
* *Integration Method:* Webhooks + REST API polling (fallback)
* *Event Types:* Issue created/updated, workflow transitions, SLA breaches
* *Authentication:* OAuth 2.0 or API tokens
* *Endpoint:* {{/webhooks/jira}}

h3. GitHub Integration
* *Integration Method:* GitHub Webhooks
* *Event Types:* Workflow runs, deployments, security alerts, PR events
* *Authentication:* HMAC signature verification
* *Endpoint:* {{/webhooks/github}}

h3. Ansible Automation Platform Integration
* *Integration Method:* Webhooks + REST API
* *Event Types:* Job failures, workflow completions, host status changes
* *Authentication:* OAuth 2.0 or API tokens
* *Endpoint:* {{/webhooks/ansible}}

h3. Azure Red Hat OpenShift Integration
* *Integration Method:* Prometheus Alertmanager webhooks + Kubernetes Watch API
* *Event Types:* Pod failures, node issues, resource constraints, deployment failures
* *Authentication:* Bearer tokens, mTLS
* *Endpoint:* {{/webhooks/openshift}}

---

h2. Event Management Layer

h3. Event Ingestion Service

{panel:title=Purpose|borderStyle=solid|borderColor=#0052CC|titleBGColor=#E3FCEF|bgColor=#FFFFFF}
Receive and validate events from source systems
{panel}

*Components:*
* *Webhook Receivers:* HTTP endpoints for each tool
* *Event Validator:* Validate event authenticity and format
* *Rate Limiter:* Prevent event flooding
* *Event Normalizer:* Convert events to standard format

*Technology Options:*
# *Option 1:* Apache Kafka (Recommended for high volume)
# *Option 2:* RabbitMQ (Good for moderate volume)
# *Option 3:* Azure Event Hubs (If using Azure infrastructure)
# *Option 4:* AWS EventBridge (If using AWS infrastructure)

h3. Event Schema

{code:language=json|title=Standard Event Format|collapse=false}
{
  "eventId": "uuid",
  "source": "jira|github|ansible|openshift",
  "eventType": "issue_created|workflow_failed|pod_crashed|...",
  "timestamp": "ISO8601",
  "priority": "critical|high|medium|low",
  "payload": {
    // Tool-specific payload
  },
  "metadata": {
    "correlationId": "uuid",
    "retryCount": 0,
    "originalTimestamp": "ISO8601"
  }
}
{code}

h3. Event Queue Management

*Primary Queue:* Active events awaiting processing
* *Partitioning:* By source system or priority
* *Retention:* 7 days
* *Replication:* Multi-replica for high availability

*Dead Letter Queue (DLQ):* Failed events after max retries
* *Retention:* 30 days
* *Manual Review:* Required for DLQ events
* *Alerting:* Notify administrators of DLQ events

*Priority Queues:*
* *Critical Queue:* Critical priority events (immediate processing)
* *High Queue:* High priority events
* *Standard Queue:* Medium/low priority events

---

h2. Event Processing Engine

h3. Event Processor Components

# *Event Filter:* Filter duplicate events, low-priority/noise events, apply business rules
# *Event Enrichment:* Add contextual information, lookup related records, add user/team information
# *Event Router:* Determine target ServiceNow table, apply routing rules, determine priority
# *Event Transformer:* Transform event to ServiceNow record format, map fields, apply validation
# *Retry Handler:* Exponential backoff retry strategy, max 5 retries, move to DLQ after max retries

h3. ServiceNow Integration Logic

*Change Request Creation Rules:*
* Ansible deployment events → Change Request
* GitHub production deployments → Change Request
* OpenShift production deployments → Change Request
* JIRA issue with "Change" label → Change Request

*Incident Creation Rules:*
* Ansible job failures → Incident
* GitHub workflow failures → Incident
* OpenShift pod crashes → Incident
* JIRA critical bugs → Incident
* Security alerts → Incident

---

h2. ServiceNow Integration Layer

h3. ServiceNow API Integration

*REST API Endpoints:*
* {{POST /api/now/table/change_request}} - Create change request
* {{POST /api/now/table/incident}} - Create incident
* {{GET /api/now/table/{table}/{sys_id}}} - Retrieve record
* {{PUT /api/now/table/{table}/{sys_id}}} - Update record

*Authentication:*
* OAuth 2.0 (recommended)
* Basic Auth (fallback)
* Service Account with appropriate roles

h3. Acknowledgment Mechanism

*Process Flow:*
# Event processor creates record in ServiceNow
# ServiceNow returns record with sys_id and number
# Processor extracts change_request.number or incident.number
# Processor sends acknowledgment back to source system
# Source system updates its record with ServiceNow reference

---

h2. Resilience and Reliability

h3. ServiceNow Unavailability Handling

*Detection:*
* Health check endpoint: {{/api/now/table/sys_user?sysparm_limit=1}}
* Health check interval: 30 seconds
* Failure threshold: 3 consecutive failures

*Behavior During Outage:*
# Events continue to be ingested into queue
# Event processor detects ServiceNow unavailability
# Events remain in queue (not processed)
# Queue continues to accumulate events
# Health check monitors ServiceNow recovery

*Recovery Process:*
# ServiceNow health check succeeds
# Event processor resumes processing
# Process events in priority order (Critical → High → Standard)
# Process backlog with rate limiting to avoid overload
# Monitor processing metrics

*Queue Capacity:*
* Maximum queue size: 1,000,000 events
* Alert threshold: 80% capacity
* Overflow handling: Reject new events or archive old events

h3. Retry Strategy

*Exponential Backoff:*
{code:language=text|title=Retry Schedule|collapse=false}
Attempt 1: Immediate
Attempt 2: 1 second delay
Attempt 3: 5 seconds delay
Attempt 4: 30 seconds delay
Attempt 5: 5 minutes delay
Attempt 6: 30 minutes delay
Max Attempts: 6
{code}

*Retry Conditions:*
* ServiceNow API timeout
* ServiceNow API 5xx errors
* Network failures
* Rate limit exceeded (429)

*No Retry Conditions:*
* ServiceNow API 4xx errors (client errors)
* Authentication failures
* Invalid data format

---

h2. Technology Stack Recommendations

h3. Option 1: Open Source Stack (Recommended)

*Event Management:*
* *Apache Kafka:* Event streaming platform
* *Kafka Connect:* Connector framework
* *Schema Registry:* Event schema management

*Event Processing:*
* *Apache Flink / Apache Storm:* Stream processing
* *Or:* Custom microservice (Node.js/Python/Java)

*Container Platform:*
* *Kubernetes:* Container orchestration
* *Docker:* Container runtime

*Monitoring:*
* *Prometheus:* Metrics collection
* *Grafana:* Visualization
* *ELK Stack:* Logging

h3. Option 2: Cloud-Native Stack

*Azure:*
* *Azure Event Hubs:* Event streaming
* *Azure Functions:* Event processing
* *Azure Service Bus:* Message queue
* *Azure Monitor:* Monitoring

*AWS:*
* *Amazon EventBridge:* Event bus
* *AWS Lambda:* Event processing
* *Amazon SQS:* Message queue
* *CloudWatch:* Monitoring

---

h2. Security Architecture

h2. Authentication and Authorization

*Source Systems → Event Ingestion:*
* JIRA: OAuth 2.0 or API tokens
* GitHub: HMAC signature verification
* Ansible: OAuth 2.0 or API tokens
* OpenShift: Bearer tokens, mTLS

*Event Processing → ServiceNow:*
* OAuth 2.0 (recommended)
* Service Account with minimal required permissions
* Token rotation and refresh

h2. Data Security

*Encryption:*
* TLS 1.3 for data in transit
* Encryption at rest for queues and databases
* Encrypted secrets management (HashiCorp Vault, AWS Secrets Manager)

---

h2. Monitoring and Observability

h2. Key Metrics

* *Event ingestion rate* (events/second)
* *Event processing latency* (p50, p95, p99)
* *Queue depth* (by priority)
* *ServiceNow API success/failure rate*
* *Acknowledgment delivery rate*
* *Dead letter queue size*
* *ServiceNow availability status*

h2. Alerting

*Critical Alerts:*
* ServiceNow unavailable
* Queue capacity > 80%
* Dead letter queue growth
* Processing latency > threshold

*Warning Alerts:*
* High retry rate
* Rate limiting encountered
* Acknowledgment delivery failures

---

h2. Integration Patterns

h2. Event-to-Ticket Mapping

||Source||Event Type||ServiceNow Table||Priority Mapping||
|JIRA|Critical Bug|Incident|Critical → 1|
|JIRA|Change Request|Change Request|High → 2|
|GitHub|Workflow Failed|Incident|Critical → 1|
|GitHub|Security Alert|Incident|Critical → 1|
|Ansible|Job Failed|Incident|High → 2|
|Ansible|Deployment|Change Request|Medium → 3|
|OpenShift|Pod CrashLoop|Incident|Critical → 1|
|OpenShift|Deployment|Change Request|High → 2|

---

h1. Document Approval

||Role||Name||Signature||Date||
|Solution Architect|[Name]|||
|Technical Lead|[Name]|||
|ServiceNow Admin|[Name]|||
|Project Manager|[Name]|||

---

h1. Document History

||Version||Date||Author||Changes||
|1.0|[Date]|[Name]|Initial architecture design|

