# Pulumi Nginx Deploy

A Pulumi project to deploy Nginx on Kubernetes.

## Description

This project uses Pulumi with Python to deploy an Nginx application to a Kubernetes cluster.

## Prerequisites

- Python 3.10+
- Pulumi CLI
- Kubernetes cluster access
- Poetry for dependency management

## Installation

1. Activate your virtual environment:
   ```bash
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

## Usage

Deploy the infrastructure:
```bash
pulumi up
```

Clean up resources:
```bash
pulumi destroy
```

## Dependencies

- pulumi (3.112.0)
- pulumi-kubernetes (4.10.0)
# pulumi-nginx-deploy
