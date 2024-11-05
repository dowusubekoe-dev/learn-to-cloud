# What is SSH

SSH stands for the secure shell protocol. SSH uses a client-server connection to set up a tunnel between a local machine (the client) and a remote machine (the server).

SSH enables you to access a remote machine, virtual machine, or container securely over a network connection. 

o connect using SSH, you must have a running SSH server. Most commonly, the connection is authenticated using SSH keys, which involves generating a public and private key-pair. Once the key-pair is generated, the public key is placed on the server, and the private key is kept secret on the client. When a connection is initiated, the server verifies that the client has the correct private key. Once verified, the client is granted access to the server, and a secure connection is established.

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

ls -a **~/.ssh**


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