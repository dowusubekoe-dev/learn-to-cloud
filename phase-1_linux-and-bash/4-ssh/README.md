# What is SSH

SSH stands for the secure shell protocol. SSH uses a client-server connection to set up a tunnel between a local machine (the client) and a remote machine (the server).

SSH enables you to access a remote machine, virtual machine, or container securely over a network connection. 

o connect using SSH, you must have a running SSH server. Most commonly, the connection is authenticated using SSH keys, which involves generating a public and private key-pair. Once the key-pair is generated, the public key is placed on the server, and the private key is kept secret on the client. When a connection is initiated, the server verifies that the client has the correct private key. Once verified, the client is granted access to the server, and a secure connection is established.
