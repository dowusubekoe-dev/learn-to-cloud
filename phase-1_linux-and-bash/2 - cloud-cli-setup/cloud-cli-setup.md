# Cloud CLI

A CLI, or Command Line Interface, is a text-based user interface that allows users to interact with a computer's operating system by entering commands:

## How it works
Users type commands into a terminal or console, which are then run by the computer.
CLIs can be used to run programs, manage files, and interact with the computer.

## Install the Azure CLI on Linux

### Option 1: Install with one command
1. Install the Azure CLI is through a script maintained by the Azure CLI team

```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```
### Option 2: Step-by-step installation
2. Get packages needed for the installation process:

```bash
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
```
3. Download and install the Microsoft signing key:

```bash
sudo mkdir -p /etc/apt/keyrings
curl -sLS https://packages.microsoft.com/keys/microsoft.asc |
gpg --dearmor | sudo tee /etc/apt/keyrings/microsoft.gpg > /dev/null
sudo chmod go+r /etc/apt/keyrings/microsoft.gpg
```

4. Add the Azure CLI software repository:

```bash
AZ_DIST=$(lsb_release -cs)
echo "Types: deb
URIs: https://packages.microsoft.com/repos/azure-cli/
Suites: ${AZ_DIST}
Components: main
Architectures: $(dpkg --print-architecture)
Signed-by: /etc/apt/keyrings/microsoft.gpg" | sudo tee /etc/apt/sources.list.d/azure-clisources
```

5. Update repository information
        
```bash
sudo apt-get update
```

6. Install the **azure-cli** package:

```bash
sudo apt-get install azure-cli
```

### Update Azure CLI

1. To update Azure CLI to the latest version, use the following command:
   
```bash
az upgrade
```

2. To update all installed packages on an Ubuntu system:
   
```bash
sudo apt-get update && sudo apt-get upgrade
```

3. To upgrade the Azure CLI only, use:
   
```bash
sudo apt-get install --only-upgrade azure-cli
```

## Install AWS Command Line Interface

1. To install the AWS CLI, run the following commands.
        
```bash
sudo curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo unzip awscliv2.zip
sudo ./aws/install
```
2. And to install it locally.

```bash
sudo curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo unzip awscliv2.zip
sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update
```

## Resources

1. [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt)

2. [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)