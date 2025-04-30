# What is SSH

SSH stands for the secure shell protocol. SSH uses a client-server connection to set up a tunnel between a local machine (the client) and a remote machine (the server).

SSH enables you to access a remote machine, virtual machine, or container securely over a network connection. 

To connect using SSH, you must have a running SSH server. Most commonly, the connection is authenticated using SSH keys, which involves generating a public and private key-pair. Once the key-pair is generated, the public key is placed on the server, and the private key is kept secret on the client. When a connection is initiated, the server verifies that the client has the correct private key. Once verified, the client is granted access to the server, and a secure connection is established.


## Steps to Connect to Your Instance Using an SSH Client

1. Begin by opening a terminal window on your local machine.

2. Utilize the `ssh` command to initiate a connection to your instance. Ensure you have the necessary details, including the path to your private key (.pem file), the username associated with the instance, and either the public DNS name or the IPv6 address. Below are examples of the commands you may use:

   **Using Public DNS**: To connect via the public DNS name, execute the following command:
   ```bash
   ssh -i /path/key-pair-name.pem instance-user-name@instance-public-dns-name
   ```

   **Using IPv6**: If your instance is assigned an IPv6 address, you can connect using the following command:
   ```bash
   ssh -i /path/key-pair-name.pem instance-user-name@instance-IPv6-address
   ```

3. Upon executing the command, you may receive a prompt similar to the following:
   ```
   The authenticity of host 'ec2-198-51-100-1.compute-1.amazonaws.com (198-51-100-1)' cannot be established.
   ECDSA key fingerprint is l4UB/neBad9tvkgJf1QZWxheQmR59WgrgzEimCG6kZY.
   Are you sure you want to continue connecting (yes/no)?
   ```

   **Optional**: It is advisable to verify that the fingerprint displayed matches the expected fingerprint. If there is a discrepancy, it may indicate a potential man-in-the-middle attack. If the fingerprints match, you may proceed to the next step. For further information, refer to the section on obtaining the instance fingerprint.

4. Type `yes` to confirm the connection.

   You should then see a message similar to the following:
   ```
   Warning: Permanently added 'ec2-198-51-100-1.compute-1.amazonaws.com' (ECDSA) to the list of known hosts.
   ```

By following these steps, you will successfully connect to your AWS Linux instance using an SSH client.


## Setting Up SSH Keys on Linux

The following commands needs to be executed when setting up SSH on a linux (Ubuntu) machine.

        ```bash
        ssh-keygen -b 4096 #this generates an RSA key pair
        ```

        ```bash
        Output
        Generating public/private rsa key pair.
        Enter file in which to save the key (/your_home/.ssh/id_rsa):
        ```
Hit **Enter** key and when prompted for a **passphrase**, hit **Enter** key twice

Copy the **Public key** to the server or node using the **ssh-copy-id** command

        ```bash
        ssh-copy-id username@remote_host
        ```

The **Public key** can be also copied using SSH

        ```bash
        cat ~/.ssh/id_rsa.pub | ssh username@remote_host "mkdir -p ~/.ssh && touch ~/.ssh/authorized_keys && chmod -R go= ~/.ssh && cat >> ~/.ssh/authorized_keys"
        ```

Manually copying of the **Public key** can be done by executing this command.

Ensure that the **~/.ssh** directory exists on the **remote server/host**

        ```bash
        ls -a ~/.ssh
        ```
Verify the content of the public key **id_rsa.pub**

        ```bash
        cat ~/.ssh/id_rsa.pub
        ```

Enter the contents of the **id_rsa.pub** file at the end of the **authorized_keys**

        ```bash
        echo public_key_string >> ~/.ssh/authorized_keys
        ```

Ensure that the **~/.ssh directory** and **authorized_keys** file have the right permissions

        ```bash
        chmod -R go= ~/.ssh
        ```

Also make sure that the **~/.ssh** directory belongs to a user but not **root**

        ```bash
        chown -R dorbsyfx:dorbsyfx ~/.ssh
        ```

Authenticating to the Ubuntu Server using SSH Keys

        ```bash
        ssh username@remote_host
        ```

Disable Password Authentication

        ```bash
        sudo nano /etc/ssh/sshd_config
        ```

Look for the line starting with **PasswordAuthentication** and comment it out or set it to **no**

Restart SSH on the server

        ```bash
        sudo systemctl restart ssh
        ```

# Connecting to a VM via SSH

To SSH into a virtual machine (VM) from your local terminal, follow these steps:

1. **Open your terminal** on your local machine.
2. **Use the SSH command** to connect to your VM. The basic syntax is:
    ```bash
    ssh username@vm_ip_address
    ```
   Replace `username` with your VM's username and `vm_ip_address` with the public IP address of your VM.

3. **Accept the SSH key fingerprint** if prompted. This is a security measure to ensure you are connecting to the correct server.

4. **Enter your password** if prompted. If you have set up SSH keys, you may not need to enter a password.

5. Once authenticated, you will have access to the VM's command line interface.

Make sure that your VM is running and that the SSH service is enabled on it.

# How to SSH using SSH keys (not passwords)

Using SSH keys for authentication is a more secure method than using passwords. Here's how to set it up:

1. **Generate SSH keys** on your local machine if you haven't already:
    ```bash
    ssh-keygen -b 4096
    ```
   Follow the prompts to save the key pair.

2. **Copy the public key** to the remote server:
    ```bash
    ssh-copy-id username@remote_host
    ```
   Replace `username` with your remote server's username and `remote_host` with its IP address.

3. **Connect to the remote server** using SSH:
    ```bash
    ssh username@remote_host
    ```
   You should be able to log in without entering a password, as long as your private key is loaded into your SSH agent.

4. **Ensure your SSH agent is running** and your key is added:
    ```bash
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_rsa
    ```

5. **Disable password authentication** on the server for added security:
    - Edit the SSH configuration file:
        ```bash
        sudo nano /etc/ssh/sshd_config
        ```
    - Set `PasswordAuthentication no` and restart the SSH service:
        ```bash
        sudo systemctl restart ssh
        ```

By following these steps, you can securely SSH into your server using SSH keys instead of passwords.