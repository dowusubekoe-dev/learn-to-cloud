# Connecting to Your Linux Instance via SSH Client

This section outlines the steps required to establish a connection to your Linux instance using an SSH client.

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
