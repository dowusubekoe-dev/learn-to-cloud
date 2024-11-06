# Linux Command Line CTF Lab - AWS

Welcome to the Linux Command Line Capture The Flag (CTF) lab! This project sets up a learning environment where you can practice your Linux command line skills by solving various challenges.

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

1. [Terraform](https://www.terraform.io/downloads.html) (version 1.9.0 or later)
2. [AWS CLI](https://aws.amazon.com/cli/) (configured with your AWS credentials)

## Getting Started

Follow these steps to set up and access your CTF lab environment:

1. Clone this repository to your local machine:

    ``` sh
    git clone https://github.com/learntocloud/ltc-linux-challenge
    cd ltc-linux-challenge/aws
    ```

2. (Optional) Modify the AWS region:
    - Open `main.tf` and change the default value of the `aws_region` variable, or
    - Create a `terraform.tfvars` file and specify your preferred region:

        ``` sh
        aws_region = "us-east-1"
        ```

3. Initialize Terraform:

    `terraform init`

4. Apply the Terraform configuration:

    `terraform apply`

    When prompted, type `yes` to confirm.

5. After the apply completes, note the `ctf_instance_public_ip` output. You'll use this to connect to your lab environment.
![Terrform Apply output](./images/terraform-apply-screenshot.png)

## Accessing the Lab Environment

To access your lab environment:

1. Use SSH to connect to the EC2 instance:

    ``` sh
      ssh ec2-user@<ctf_instance_public_ip>
    ```

2. When prompted for a password, enter: `CTFpassword123!`
3. Once logged in, you'll see a welcome message with instructions for your first challenge.
![ssh into the instance](./images/ssh-screenshot.png)

## Personal Challenges

1. Syntax error

```bash
Error: Invalid reference
│   on main.tf line 107, in resource "aws_instance" "ctf_instance":
│  107:   key_name      = aws_login
```

2. Per instructions, a **key pair** was not to be included. I update the **main.tf** in the **aws_instance** resource block and added the **key_name** attribute and got the error below

```bash
Error: Reference to undeclared resource
│   on main.tf line 107, in resource "aws_instance" "ctf_instance":
│  107:   key_name      = aws_login.pem
│ A managed resource "aws_login" "pem" has not been declared in the root module.
```

3. Security Concerns: I got this warning in the AWS console

**"Port 22 (SSH) is open to all IPv4 addresses. Port 22 (SSH) is currently open to all IPv4 addresses, indicated by 0.0.0.0/0 in the inbound rule in your security group."**

4. Exposed **key pair** file. I added the key pair file to the project in the AWS folder.


### Resolution 

1. Updated the **main.tf** and the **aws_instance** resource block

```hcl
resource "aws_instance" "ctf_instance" {
  ami           = data.aws_ami.amazon_linux_2.id  # Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type
  instance_type = "t2.micro"
  key_name      = "your-keypair-name"  # Replace with your existing key pair name with double quotes

  vpc_security_group_ids       = [aws_security_group.ctf_sg.id]
  subnet_id                    = aws_subnet.ctf_subnet.id
  associate_public_ip_address  = true
  user_data                    = data.template_file.user_data.rendered

  tags = {
    Name = "CTF Lab Instance"
  }
}
```

2. Downloaded the **key pair.pem** file from AWS to my Windows 10 laptop and saved it in the **.ssh** folder. I then used the **scp** command to copy the file to from **C:\Users\Username\.ssh** to my Ubuntu server on **/home/username/username** by running the command in  **Powershell** with Admin privilages.

```bash
scp .\Users\username\.ssh\<key-pair.pem> server-username@192.xx.xx.xx:/home/username/
```

3. From the AWS Console, I went into the **Security Groups** to verify **My IP** information under the **Inbound rules** for **SSH**, and updated the **aws_security_group** resource block for **SSH**

```hcl
resource "aws_security_group" "ctf_sg" {
  name        = "ctf_sg"
  description = "Security group for CTF lab"
  vpc_id      = aws_vpc.ctf_vpc.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["203.0.113.4/32"]  # Replace with your IP address or IP range
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "CTF Lab Security Group"
  }
}
```

In addition, I enabled **Dynamic IP** input by creating another variable called **variable "trusted_ip"** and added the code below;

```hcl
variable "trusted_ip" {
  description = "The IP address or CIDR block allowed to access SSH"
  type        = string
  default     = "203.0.113.4/32"  # Replace with your IP
}
```

Then finally updated the **security group** to reference this variable:

```hcl
cidr_blocks = [var.trusted_ip]
```

Implementing this will help secure SSH access to only specified IP addresses, significantly reducing the risk of unauthorized access to your instance.

**Remember to save all changes and rum the *terraform apply* command**

4. In order not to exposed the **key pair** file, I updated the **.gitignore** file and added this;

```bash
# Ignore .pem key pair file
*.pem
```

## Challenges

Your CTF lab consists of 7 challenges, each testing different Linux command line skills. The challenges are:

1. Find a hidden file
2. Locate a file with "secret" in its name
3. Find the largest file in a specific directory
4. Identify a user with a specific UID
5. Locate a file with specific permissions
6. Find a process running on a specific port
7. Decode a base64 encoded message

Work through these challenges to improve your command line skills and find all the flags!

## Cleaning Up

When you're done with the lab, don't forget to destroy the AWS resources to avoid unnecessary charges:

`terraform destroy`

Type `yes` when prompted to confirm.

## Security Note

This lab is designed for learning purposes and uses a password-based login for simplicity. In real-world scenarios, key-based authentication is recommended for better security.

## Troubleshooting

If you encounter any issues:

1. Ensure your AWS CLI is correctly configured with your credentials.
2. Check that you're using a compatible Terraform version.
3. Verify that you have the necessary AWS permissions to create the required resources.

If problems persist, please open an issue in this repository.

Happy learning, and good luck with your CTF challenges!
