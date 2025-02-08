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


## Install Terraform

To use Terraform you will need to install it. HashiCorp distributes Terraform as a [binary package](https://developer.hashicorp.com/terraform/install). Terraform can also be installed by using popular package managers.

For this project, an Ubuntu server will be used as the control machine.

1. Verify HashiCorp's GPG signature and install HashiCorp's Debian package repo

```bash
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common
```

2. Install the HashiCorp [GPG key](https://apt.releases.hashicorp.com/gpg)

```bash
wget -O- https://apt.releases.hashicorp.com/gpg | \
gpg --dearmor | \
sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null
```

3. Verify the key's fingerprint.
 
```bash
gpg --no-default-keyring \
--keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
--fingerprint
```

4. Add the official HashiCorp repository to your system.
        
```bash
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/hashicorp.list
```

5. Download the package information from HashiCorp.

```bash
sudo apt update
```

6. Install Terraform from the new repository.

```bash
sudo apt-get install terraform
```

7. Verify that the installation worked

```bash
terraform -help
```

*Troubleshoot: If you get an error that terraform could not be found, your PATH environment variable was not set up properly. Please go back and ensure that your PATH variable contains the directory where Terraform was installed*

8. Enable tab completion

```bash
touch ~/.bashrc
```

```bash
terraform -install-autocomplete
```

## Terraform Basic Commands

1. Initialize the directory
Initializing a configuration directory downloads and installs the providers defined in the configuration.

```tf
terraform init
```

2. Format and validate the configuration
The **terraform fmt** command automatically updates configurations in the current directory for readability and consistency.

```tf
terraform fmt
```

3. Create infrastructure
Apply the configuration now with the terraform apply command.

```tf
terraform apply
```

4. Inspect the current state using 

```tf
terraform show
```

5. Validate Command
This command validates the configuration files in a directory. Validate runs checks that verify whether a configuration is syntactically valid and internally consistent, regardless of any provided variables or existing state.

```tf
terraform validate
```

6. Plan Your Infrastructure
Plan will generate an execution plan.

```tf
terraform plan
```
Save the plan file to a given path.

```tf
terraform plan -out=<path>
```
Create a plan to destroy all objects rather than the usual actions.

```tf
terraform plan -destroy
```

7. Deploy Infrastructure
Create or update infrastructure depending on the configuration files.

```tf
terraform apply
```
Apply changes without having to interactively type ‘yes’ to the plan. Useful in automation CI/CD pipelines.

```tf
terraform apply -auto-approve
```

8. Destroy Infrastructure
Destroy the infrastructure managed by Terraform.

```tf
terraform destroy
```
Destroy the infrastructure without having to interactively type ‘yes’ to the plan. Useful in automation CI/CD pipelines.

```tf
terraform destroy --auto-approve
```

9. Refresh the State File
Modify the state file with updated metadata containing information on the resources being managed in Terraform.

```tf
terraform refresh
```

## Inspect state
When you applied your configuration, Terraform wrote data into a file called **terraform.tfstate**. Terraform stores the IDs and properties of the resources it manages in this file, so that it can update or destroy those resources going forward. The **state file** must be stored securely and access should be restrict to only trusted team members who need to manage the infrastructure.


## Resources

1. [Install Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)

2. [Terraform Cheat Sheet](https://spacelift.io/blog/terraform-commands-cheat-sheet)


