# What is Kubernetes

Kubernetes is a platform for running and managing containerized applications.

Containers package an application and its dependencies. Kubernetes helps deploy those containers, keep them running, scale them when traffic changes, and manage them across multiple machines.

Source: [Kubernetes Documentation - Overview](https://kubernetes.io/docs/concepts/overview/)

## Simple Definition

| Term | Beginner-friendly meaning |
| --- | --- |
| **Kubernetes** | A tool that manages containers across a group of machines. |
| **Orchestration** | Automatically coordinating how containers are deployed, started, stopped, scaled, and replaced. |
| **Containerized application** | An application packaged in a container image so it can run consistently across environments. |

## Why Kubernetes Matters

Running one container is usually simple. Running many containers in production is harder.

Kubernetes helps answer questions like:

- Where should each container run?
- What happens if a container crashes?
- How do we run more copies when traffic increases?
- How do users reach the correct container?
- How do we update the application without taking everything down?

## Core Kubernetes Concepts

| Concept | What it means |
| --- | --- |
| **Cluster** | A group of machines that Kubernetes manages. |
| **Node** | One machine in the cluster. A node can run containers. |
| **Pod** | The smallest unit Kubernetes runs. A pod usually contains one application container. |
| **Deployment** | A Kubernetes object that manages running copies of an application. |
| **Service** | A stable way to reach pods, even if the pods are replaced or moved. |
| **Namespace** | A way to organize resources inside a cluster. |

## What Kubernetes Does

| Feature | Beginner-friendly explanation |
| --- | --- |
| **Deployment** | Starts containers from container images and runs them in the cluster. |
| **Scaling** | Runs more or fewer copies of an application based on need. |
| **Self-healing** | Restarts or replaces containers when they fail. |
| **Rollouts** | Updates an application in a controlled way. |
| **Rollbacks** | Moves back to an older version if a release has problems. |
| **Service discovery** | Helps applications find and communicate with each other. |
| **Load balancing** | Spreads traffic across multiple running copies of an application. |
| **Configuration and secrets management** | Stores settings and sensitive values separately from the container image. |

## Desired State

Kubernetes works by using the idea of **desired state**.

Desired state means you tell Kubernetes what you want the system to look like. Kubernetes then works to make the real system match that goal.

Example:

```text
I want 3 copies of my web app running.
```

If one copy crashes, Kubernetes notices that only 2 copies are running. It starts another one so the system goes back to 3 copies.

## Beginner Example

Imagine you have a web application packaged in a container image.

Without Kubernetes, you may need to manually:

1. Choose which server runs the container.
2. Start the container.
3. Restart it if it crashes.
4. Add more containers when traffic increases.
5. Update containers when a new version is released.

With Kubernetes, you describe what you want, and Kubernetes helps manage the work automatically.

For example:

```text
Run my web app.
Keep 3 copies running.
Restart failed copies.
Send traffic to healthy copies.
Roll out updates carefully.
```

## Kubernetes and Containers

| Containers | Kubernetes |
| --- | --- |
| Package an application and its dependencies. | Runs and manages containers in production. |
| Help software run consistently. | Helps software stay available and scalable. |
| Usually focus on one application process. | Coordinates many containers across many machines. |

## What Kubernetes Is Not

Kubernetes is powerful, but it does not do everything by itself.

| Kubernetes is not | What that means |
| --- | --- |
| **A tool that writes your code** | Developers still build the application. |
| **A CI/CD system by itself** | Teams still use pipelines to build, test, and release code. |
| **A complete monitoring solution by itself** | Teams still choose logging, monitoring, and alerting tools. |
| **A database by itself** | Databases can run on Kubernetes, but Kubernetes is not the database. |

## Key Idea

Kubernetes helps teams run containerized applications reliably.

It is used for:

- Deploying containers
- Scaling applications
- Restarting failed containers
- Balancing traffic
- Managing updates
- Keeping the real system close to the desired state
