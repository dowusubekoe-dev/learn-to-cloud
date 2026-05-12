# What is Infrastructure as Code

Infrastructure as Code, also called IaC, means managing technology resources with code instead of setting them up manually.

Infrastructure includes things like servers, databases, networks, storage, and cloud services. Instead of clicking through a cloud console every time you need something, you write instructions in a file. A tool can then read that file and create or update the infrastructure for you.

Source: [HashiCorp - What is infrastructure as code?](https://www.hashicorp.com/en/resources/what-is-infrastructure-as-code)

## Simple Definition

| Term | Beginner-friendly meaning |
| --- | --- |
| **Infrastructure** | The technology your application needs to run, such as servers, databases, and networks. |
| **Code** | A file that describes what infrastructure should exist. |
| **Infrastructure as Code** | A way to create and manage infrastructure using files instead of manual steps. |

## Manual Infrastructure vs Infrastructure as Code

| Manual Setup | Infrastructure as Code |
| --- | --- |
| A person clicks buttons in a cloud console. | A tool reads a configuration file. |
| Steps can be forgotten or done differently each time. | The same instructions can be reused every time. |
| It is harder to know who changed what. | Changes can be tracked in Git. |
| Recreating an environment can take a long time. | Environments can be recreated faster and more consistently. |

## Why Infrastructure as Code Matters

| Benefit | Why it helps |
| --- | --- |
| **Consistency** | The same code can create the same type of environment again and again. |
| **Speed** | Teams can create infrastructure faster than doing everything by hand. |
| **Tracking** | Infrastructure changes can be stored in Git, so teams can see what changed and when. |
| **Automation** | Repeated tasks can be handled by tools instead of people doing each step manually. |
| **Collaboration** | Teams can review infrastructure changes before they are applied. |

## Beginner Example

Imagine your application needs a web server.

Without Infrastructure as Code, someone might:

1. Log in to a cloud provider.
2. Click through several screens.
3. Choose a server size.
4. Configure networking.
5. Start the server.

With Infrastructure as Code, the team writes those requirements in a file. Then an IaC tool can create the server from that file.

This makes the setup easier to repeat, review, and improve.

## Common Infrastructure as Code Tools

| Tool | What it is commonly used for |
| --- | --- |
| **Terraform** | Creating and managing cloud infrastructure across different providers. |
| **CloudFormation** | Managing AWS infrastructure using templates. |
| **Ansible** | Automating server configuration and software setup. |

## Key Idea

Infrastructure as Code helps teams treat infrastructure the same way they treat application code.

That means infrastructure can be:

- Written in files
- Stored in version control
- Reviewed by teammates
- Reused across environments
- Automated through pipelines
