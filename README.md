# DevSecOps Compliance as Code Pipeline

## Overview
This project demonstrates how security and compliance checks can be automated within a CI/CD pipeline.

## Key Features
- Automated vulnerability scanning using Trivy
- Docker image security analysis
- CI/CD pipeline using GitHub Actions
- Detection of hardcoded secrets (compliance violation)

## Tools Used
- GitHub Actions
- Docker
- Trivy
- Python (Flask)

## Outcome
This project simulates how organizations can shift from manual audits to continuous compliance by embedding controls directly into the development pipeline.

## Compliance Controls Implemented
- ❌ Build fails if HIGH or CRITICAL vulnerabilities are detected
- 📄 Automated generation of security scan reports
- 🔍 Continuous scanning of source code and container images

## Audit Value
This pipeline demonstrates how compliance requirements can be:
- Enforced automatically
- Monitored continuously
- Documented with verifiable evidence