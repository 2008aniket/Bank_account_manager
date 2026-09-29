# Bank Management System (BMS) - Project Statement

## 1. Executive Summary
The **Bank Management System (BMS)** is an enterprise-grade core banking application designed to handle customer account operations, transaction processing, credit management, and regulatory audit tracking with high concurrency and fault tolerance.

> **Project Code:** BMS-CORE-2025  
> **Classification:** Confidential Internal Documentation  
> **Target Release:** Q3 2025

---

## 2. System Architecture & Tech Stack
The architecture relies on a decoupled microservices design ensuring high availability and ACID transaction guarantees.

- **Frontend Interface:** React 18 / TypeScript / Tailwind CSS
- **Backend API Layer:** Node.js (NestJS REST & gRPC API Gateway)
- **Database Engine:** PostgreSQL 16 (Primary Transactional Ledger)
- **In-Memory Cache:** Redis Enterprise (Session Store & Rate Limiting)
- **Security & Compliance:** OAuth2 + JWT, AES-256 Encryption at Rest, TLS 1.3

---

## 3. Core Functional Requirements

### 3.1 Account Management
- Support for Savings, Checking, and Fixed Deposit accounts.
- Automated IBAN and Account Number generation upon KYC verification.
- Account state machine: `PENDING`, `ACTIVE`, `FROZEN`, `CLOSED`.

### 3.2 Transaction Engine
- Real-time processing for Deposits, Withdrawals, and Peer-to-Peer Transfers.
- Strict daily transaction threshold enforcement ($10,000 P2P default).
- Two-phase commit (2PC) for cross-branch inter-bank transfers.

### 3.3 Credit & Loan Module
- Automated EMI calculation based on reducing balance interest.
- Credit score verification integration with credit bureaus.
- Multi-tier approval workflow for loans exceeding $50,000.

---

## 4. Non-Functional Requirements & Metrics

| Metric Category | Requirement Specification |
| :--- | :--- |
| **API Latency** | 95th percentile response time < 150ms |
| **Availability** | 99.99% operational uptime SLA |
| **Concurrency** | Peak load support for 5,000 transactions/sec |
| **Audit Compliance** | Immutable write-once audit logs (PCI-DSS & GDPR compliant) |

---

## 5. Deployment & Security Standards
1. All API endpoints require MFA token authorization.
2. Automated daily zero-downtime backups with point-in-time recovery (PITR).
3. Full integration with centralized SIEM logging systems.
