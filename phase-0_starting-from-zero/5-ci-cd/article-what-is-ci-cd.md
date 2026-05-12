# What is CI/CD

CI/CD is a DevOps practice that helps teams build, test, and release software automatically.

Instead of doing every release step by hand, teams create a pipeline. A pipeline is a set of automated steps that runs whenever code changes.

Source: [Red Hat - What is CI/CD?](https://www.redhat.com/en/topics/devops/what-is-ci-cd)

## Simple Definition

| Term | Meaning |
| --- | --- |
| **CI** | Continuous Integration. Developers frequently merge code changes into a shared repository. |
| **CD** | Continuous Delivery or Continuous Deployment. Code changes are prepared for release or automatically released to production. |
| **Pipeline** | The automated workflow that builds, tests, and releases the application. |

## Continuous Integration

Continuous Integration helps teams find problems early by automatically checking new code when it is added to the shared project.

| Step | What happens |
| --- | --- |
| **Code is pushed** | A developer sends code changes to the shared repository. |
| **Code is merged often** | Developers avoid waiting too long before combining their work with the rest of the team. |
| **Build runs** | The application is prepared so the team knows whether the code can still run. |
| **Tests run** | Automated tests check whether the new change broke existing features. |
| **Feedback is given** | The team sees whether the change passed or failed. |

The goal of CI is to avoid large, painful merge problems. Smaller changes are easier to test, review, and fix.

## Continuous Delivery and Continuous Deployment

| Practice | Beginner-friendly meaning |
| --- | --- |
| **Continuous Delivery** | Code is automatically built, tested, and prepared for release. A person usually approves when it goes to production. |
| **Continuous Deployment** | Code is automatically built, tested, and released to production without manual approval. |

Continuous delivery keeps the codebase ready to deploy. Continuous deployment goes one step further by automatically releasing the change when it passes the pipeline.

## Basic CI/CD Pipeline

| Stage | What it does |
| --- | --- |
| **Commit** | A developer saves and pushes code changes. |
| **Build** | The pipeline prepares the application so it can run. |
| **Test** | Automated tests check the code for problems. |
| **Security checks** | The pipeline can scan for unsafe code, vulnerable dependencies, or policy problems. |
| **Package** | The application is bundled into a deployable version, such as a container image. |
| **Deliver** | The tested build is stored somewhere it can be released from, such as a repository or registry. |
| **Deploy** | The application is released to an environment, such as staging or production. |
| **Monitor** | The team watches the application after release to make sure it is healthy. |

## Why CI/CD Matters

| Benefit | Why it helps |
| --- | --- |
| **Faster releases** | Teams can ship smaller changes more often. |
| **Fewer manual steps** | Automation reduces repeated human work and mistakes. |
| **Earlier feedback** | Tests and checks can catch problems before users see them. |
| **Less risky deployments** | Small, tested changes are usually safer than large releases. |
| **Better collaboration** | Development and operations teams share one repeatable release process. |
| **Happier users** | Teams can respond to bugs, feedback, and feature requests more quickly. |

## CI/CD and Security

Security should be part of the pipeline, not something added only at the end.

| Security Practice | What it helps prevent |
| --- | --- |
| **Dependency scanning** | Finds known vulnerabilities in third-party packages. |
| **Secret scanning** | Helps catch passwords, keys, or tokens before they are exposed. |
| **Code scanning** | Looks for risky patterns or security issues in the source code. |
| **Approval steps** | Adds review before sensitive production releases. |

## Beginner Example

Imagine a developer fixes a typo on a website.

With CI/CD:

1. The developer pushes the change to Git.
2. The CI/CD pipeline starts automatically.
3. The app is built.
4. Tests run to check that the website still works.
5. Security checks can run.
6. The update is prepared for release.
7. The update is deployed manually or automatically, depending on the team's CD process.

## Key Idea

CI/CD helps teams release software faster and more reliably.

It works best when teams make small changes, test them automatically, and use a repeatable pipeline to move code toward production.

**Code change** -> **Build** -> **Test** -> **Security check** -> **Deliver** -> **Deploy**
