# Infrastructure As A Code

"**Infrastructure as code**" is used in managing large-scale, distributed systems, cloud-native applications, and service-based architectures

**Infrastructure as code** is a mainstream pattern for managing infrastructure with configuration files rather than through a graphical user interface or through manual command line script sequences.

**Terraform** is most commonly used **infrastruction as code** provisioning engine.


## Key Changes

- **IaC** support versioning.
- **Reusability of the code** is also achievable.
- Ability to **automate** deployment of the infrastructure.

## Manage any infrastructure

Terraform plugins called **providers** let Terraform interact with cloud platforms and other services via their application programming interfaces (APIs). The **providers** for many of the platforms and services can be found in [Terraform Registry](https://registry.terraform.io/browse/providers).

## Standardize your deployment workflow

Providers define individual units of infrastructure, for example compute instances or private networks, as resources. Resources from different providers can be composed into reusable **Terraform configurations** called **modules**. Terraform providers automatically calculate dependencies between resources to **create** or **destroy** **infrastructure** in the correct order.

Terraform's configuration language is declarative (describes the desired end-state for an infrastructure), hence no need to follow a procedural programming language that resquire step-by-step instructions to perform a task.

To deploy infrastructure with Terraform:

- **Scope** - Identify the infrastructure for your project.
- **Author** - Write the configuration for your infrastructure.
- **Initialize** - Install the plugins Terraform needs to manage the infrastructure.
- **Plan** - Preview the changes Terraform will make to match your configuration.
- **Apply** - Make the planned changes.


## Track your infrastructure

Terraform keeps track of your real infrastructure in a state file. Terraform uses the state file to determine the changes that needs to be made to the infrastructure so that it matches the configuration.


## Collaborate

Terraform allows collaborate on the infrastructure with its remote state backends. When developers use HCP Terraform, they can securely share the state with their teammates, provide a stable environment for Terraform to run in, and prevent race conditions when multiple developers in a team make configuration changes at once.

You can also connect HCP Terraform to version control systems like GitHub, GitLab, which allow it to automatically propose infrastructure changes when a commit is made on the configuration changes to VCS.

