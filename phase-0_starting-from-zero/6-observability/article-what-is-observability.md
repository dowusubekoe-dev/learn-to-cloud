# What is Observability

Observability means understanding what is happening inside a system by looking at the information it produces.

In production, you usually cannot stop the application and inspect everything by hand. Instead, teams use observability data to monitor the system, find problems, and troubleshoot issues while users are using the application.

Source: [IBM - What is observability?](https://www.ibm.com/think/topics/observability)

## Simple Definition

| Term | Beginner-friendly meaning |
| --- | --- |
| **Production** | The live environment where real users use the application. |
| **Telemetry** | Data produced by an application or system that helps explain what is happening. |
| **Observability** | The ability to understand system health and behavior by using telemetry data. |

## The Three Main Signals

Observability often focuses on three important types of data: logs, metrics, and traces.

| Signal | What it means | Beginner example |
| --- | --- | --- |
| **Logs** | Time-stamped records of events that happened in the system. | "User login failed" or "Database connection timed out." |
| **Metrics** | Numbers that show system health over time. | CPU usage, memory usage, error rate, or response time. |
| **Traces** | A map of the path a request takes through different parts of an application. | A checkout request moving from the website, to the payment service, to the database. |

## Logs

Logs help you answer: **What happened?**

| What logs help with | Why it matters |
| --- | --- |
| **Troubleshooting errors** | Logs can show error messages and details about what failed. |
| **Debugging application behavior** | Logs help developers understand what the application was doing at a specific time. |
| **Finding patterns** | Repeated log messages can show recurring problems. |

Example:

```text
2026-05-12 10:15:22 ERROR Payment service timeout for order 12345
```

This log tells the team when the error happened, which service had a problem, and which order was affected.

## Metrics

Metrics help you answer: **Is the system healthy?**

| Metric | What it can tell you |
| --- | --- |
| **CPU usage** | Whether a server or container is working too hard. |
| **Memory usage** | Whether the application is using too much memory. |
| **Error rate** | How often requests are failing. |
| **Latency** | How long requests take to complete. |
| **Availability** | Whether the system is up and reachable. |

Metrics are useful for dashboards and alerts because they show trends over time.

For example, if response time suddenly increases, users may start experiencing a slow website.

## Traces

Traces help you answer: **Where did the problem happen?**

Modern applications often have many services working together. A trace follows one request through those services.

| Trace detail | What it shows |
| --- | --- |
| **Request path** | Which services handled the request. |
| **Timing** | How long each service took. |
| **Failures** | Which part of the request failed. |
| **Dependencies** | Which services rely on each other. |

Example:

```text
User checkout -> Cart service -> Payment service -> Database
```

If checkout is slow, a trace can help show whether the delay happened in the cart service, payment service, database, or somewhere else.

## Logs vs Metrics vs Traces

| Signal | Best for answering |
| --- | --- |
| **Logs** | What happened? |
| **Metrics** | Is the system healthy? |
| **Traces** | Where did the problem happen? |

Teams usually need all three because each one gives a different view of the system.

## Basic Troubleshooting Workflow

| Step | What the team does |
| --- | --- |
| **1. Notice a problem** | An alert, user report, or dashboard shows that something is wrong. |
| **2. Check metrics** | The team looks for changes in error rate, latency, CPU, memory, or availability. |
| **3. Review logs** | The team searches for error messages or unusual events. |
| **4. Follow traces** | The team checks where a request slowed down or failed. |
| **5. Find the root cause** | The team identifies the service, code, or infrastructure causing the issue. |
| **6. Fix and learn** | The team resolves the problem and improves monitoring for next time. |

## Why Observability Matters

| Benefit | Why it helps |
| --- | --- |
| **Faster troubleshooting** | Teams can move from "something is wrong" to "this is the cause" more quickly. |
| **Less downtime** | Problems can be found and fixed before they affect more users. |
| **Better user experience** | Teams can see when users are experiencing errors or slow performance. |
| **Better production confidence** | Teams can release changes and monitor how the system behaves afterward. |
| **Improved teamwork** | Developers, operations, and support teams can look at the same data during incidents. |

## Key Idea

Observability helps teams understand production systems by using the data those systems already produce.

The three most important signals are:

- **Logs:** what happened
- **Metrics:** how healthy the system is
- **Traces:** where a request went and where it had problems
