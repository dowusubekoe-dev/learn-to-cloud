# Phase 1: Linux Command Line CTF Challenge

This set of progressive Capture The Flag (CTF) challenges will test your Linux command line skills. Each challenge builds upon previous concepts while introducing new ones. All flags follow the format `CTF{some_text_here}`.

> [!IMPORTANT]  
> Please complete [Phase 1 Guide](https://learntocloud.guide/phase1/) before attempting these challenges. Do not share solutions publicly - focus on sharing your learning journey instead.

## Flag Submission

Submit flags using the `verify` command:

- Check progress: `verify progress`
- Submit a flag: `verify [challenge_number] [flag]`
- Test the system: `verify 0 CTF{example}`

Example: `verify 0 CTF{example}`

```
ctf_user@ctf-vm:~$ verify 0 CTF{example}
✓ Example flag verified! Now try finding real flags.
```

## Environment Setup

Follow the setup guide for your preferred cloud provider:

- [AWS](./aws/README.md)
- [Azure](./azure/README.md)

## Challenges

### Beginner Level

#### Challenge 1: The Hidden File

Find and read a hidden file in the `ctf_challenges` directory.

- **Skills**: Basic file listing, hidden files concept
- **Hint**: Hidden files in Linux start with a special character

##### Solution

```bash
cd ctf_challenges # change to the ctf_challenges directory
```

```bash
ls -la # list all files in the ctf_challenges directory
```

```bash
cat .hidden_flag # CTF{finding_hidden_treasures}
```

```bash
verify 1 CTF{finding_hidden_treasures} # verify the flag
```

---

#### Challenge 2: The Secret File

Locate a file containing "secret" in its name within /home/ctf_user.

- **Skills**: File searching, directory navigation
- **Hint**: Explore commands that can search through directories

##### Solution

```bash
cd ctf_challenges # change to the ctf_challenges directory. 
```

```bash
find /home/ctf_user -type f -name "*secret*" # find the file containing "secret" in its name. 
# /home/ctf_user/documents/projects/backup/secret_notes.txt  
```

```bash
cat /home/ctf_user/documents/projects/backup/secret_notes.txt # CTF{search_and_discover}
```

```bash
verify 2 CTF{search_and_discover} # verify the flag
```

---

### Intermediate Level

#### Challenge 3: The Largest Log

Identify and read the largest file in /var/log.

- **Skills**: File size analysis, sorting, log navigation
- **Hint**: Look into commands that display file sizes

##### Solution

```bash
ls -lh /var/log # list all files in the /var/log directory and show their sizes
```

```bash
sudo cat /var/log/large_log_file.log | grep -a "CTF" # CTF{size_matters_in_linux}
```

```bash
verify 3 CTF{size_matters_in_linux} # verify the flag
```

---

#### Challenge 4: The User Detective

Find a flag in the .profile of the user with UID 1002.

- **Skills**: User management, system files, permissions
- **Hint**: System files contain user information

##### Solution

```bash
cat /etc/passwd # list all users and their information
```

```bash
grep "1002" /etc/passwd # flag_user:x:1002:1002::/home/flag_user:/bin/sh
```

```bash
sudo grep "CTF{" /home/flag_user/.profile # CTF{user_enumeration_expert}
```

```bash
verify 4 CTF{user_enumeration_expert} # verify the flag
```

#### Challenge 5: The Permissive File

Find a root-owned file with 777 permissions. The flag is the contents of this file.

- **Skills**: Permission understanding, advanced file searching
- **Hint**: Consider both ownership and permission patterns

##### Solution

```bash
sudo su - # switch to the root user
```

```bash
find / -type f -user root -perm 777 -exec cat {} + # find the file with root ownership and 777 permissions

# - `find /`: Start searching from the root directory. You can replace `/` with a specific directory if you want to limit the search.
# -type f: Look for files only.
# -user root: Find files owned by the user root.
# -perm 777: Find files with 777 permissions.
# -exec cat {}: For each file found, execute the cat command to display its contents.
# +: This allows find to pass multiple files to cat at once, which is more efficient.
```

```bash
verify 5 CTF{permission_sleuth} # verify the flag
```

---

### Advanced Level

#### Challenge 6: The Hidden Service

Identify a process on port 8080 and retrieve its flag.

- **Skills**: Process management, networking tools, service inspection
- **Hint**: Network diagnostic tools can reveal running services. Port 8080 is often used for HTTP

##### Solution

```bash
netstat -tuln | grep ':8080'     # list all processes on port 8080. tcp   0   0 0.0.0.0:8080   0.0.0.0:*  LISTEN 
```

```bash
ss -tuln | grep ':8080' # list all processes on port 8080. tcp   LISTEN 0   1    0.0.0.0:8080   0.0.0.0:*
```

```bash
curl http://localhost:8080 # CTF{network_detective}
```

```bash
verify 6 CTF{network_detective} # verify the flag
```

---
#### Challenge 7: The Encoded Secret

Decode a base64-encoded flag.

- **Skills**: Encoding/decoding, command piping
- **Hint**: Linux provides built-in encoding tools

##### Solution

```bash
cd ctf_challenges # change to the ctf_challenges directory
```

```bash
cat encoded_flag.txt # Display the contents of the encoded_flag.txt file
```

```bash
echo "UTFSR2UyUmxZMjlrYVc1blgyMWhjM1JsY24wSwo=" | base64 --decode # Q1RGe2RlY29kaW5nX21hc3Rlcn0K decode the base64-encoded flag.
```

```bash
echo "Q1RGe2RlY29kaW5nX21hc3Rlcn0K" | base64 --decode # CTF{decoding_master} re-decode the base64-decoded flag.
```

```bash
verify 7 CTF{decoding_master} # verify the flag
```

```bash
#!/bin/bash

# Prompt the user to enter a Base64-encoded string
read -p "Enter the Base64-encoded string: " encoded_string

# Decode the Base64 string
decoded_string=$(echo "$encoded_string" | base64 --decode)

# Print the decoded string
echo "Decoded string: $decoded_string"

# Decode the Base64 string
decoded_string=$(echo "$decoded_string" | base64 --decode)

# Use grep to find hidden text starting with CTF
echo "$decoded_string"

# Check if hidden text was found and print it
if [ -n "$decoded_string" ]; then
    echo "Found hidden string: $decoded_string"
else
    echo "No hidden text found."
fi
``` 

#### Challenge 8: SSH Key Authentication

Configure SSH key authentication and find a hidden flag.

- **Skills**: SSH configuration, key management, security practices
- **Hint**: Pay attention to file permissions and hidden directories

##### Solution
- From the local machine, generate an SSH key pair.

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
- Save the key in `~/.ssh/id_ed25519` (default location).

```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@target_host # Copy the public key to the target host.(EC2 instance)
```
- If ssh-copy-id is unavailable, manually add the public key to the server:

```bash
cat ~/.ssh/id_ed25519.pub | ssh user@target_host "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
```
- On the target machine, verify the permissions:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

- SSH into the Target Machine. Now, attempt to log in using the key:

```bash
ssh -i ~/.ssh/id_ed25519 user@target_host
```

```bash
ls -la # Find the hidden files or directories.
```

- Use grep to look for flag-related files:

```bash
grep -r "CTF{" /home/ctf_user/ # CTF{ssh_security_master}
```

```bash
verify 8 CTF{ssh_security_master} # verify the flag
```

#### Challenge 9: DNS troubleshooting
Someone modified a critical DNS configuration file. Fix it to reveal the flag.

- **Skills**: DNS troubleshooting, file editing
- **Hint**: Compare the current configuration with its backup to understand what has changed.

##### Solution
- Identify the DNS Configuration File: The primary DNS configuration file in most Linux distributions is likely located at `/etc/resolv.conf`
- Command: `ls -l /etc/resolv.conf`
- Also confirm if it a symlink:- Command: `readlink /etc/resolv.conf`
- Locate and Examine the Backup: Command: `ls -l /etc/resolv.conf.*`
- Compare Files: Command (using diff): `diff /etc/resolv.conf /etc/resolv.conf.bak`
- Command (using vimdiff): `vimdiff /etc/resolv.conf /etc/resolv.conf.bak`
- Edit and save the changed DNS file

```bash
verify 9 CTF{dns_name} # verify the flag
```

#### Challenge 10: Remote upload
Transfer any file to the ctf_challenges directory to trigger the flag.

- **Skills**: Upload files to remote servers
- **Hint**: Make use of standard file transfer methods available to you.

##### Solution
- **scp (Secure Copy)**:
Description: A command-line tool that securely copies files between hosts using the SSH (Secure Shell) protocol. It encrypts the data transfer. This is the most widely used and often preferred method because of its security.

- **Syntax**:
Copying from local to remote: scp [options] local_file user@remote_host:remote_directory
Copying from remote to local: scp [options] user@remote_host:remote_file local_directory

- **Examples**:

`scp myfile.txt user@192.168.1.100:/home/user/documents/` (Copying from local to a remote server)

`scp -r /home/local_user/projects user@remote_host:/opt/backups/` (Copying a directory recursively)

`scp -P 2222 myfile.txt user@remote_host:/tmp/` (Specifying a different SSH port on the remote host)

`scp -i ~/.ssh/id_rsa myfile.txt user@remote_host:/tmp/` (using an ssh key)

##### Solution
- Navigate to the directory you want to copy file from on the local machine
- Run the scp command: `scp aws-terraform-kp.pem ctf_user@44.204.170.155:/home/ctf_user/ctf_challenges/`

```bash
Here is your flag: CTF{network_copy} # A new file named aws-terraform-kp.pem has been added to /home/ctf_user/ctf_challenges.
```
```bash
verify 10 CTF{network_copy}
```

#### Challenge 11: Web Configuration
The web server is running on a non-standard port. Find and fix it.

- **Skills**: Nginx configuration, service management
- **Hint**: Review the web server's configuration files for unusual port assignments and remember to restart the service after making any changes.

##### Solution
1. Apache HTTP Server:

Main Configuration File: `/etc/apache2/apache2.conf` 

For (Debian/Ubuntu/Mint) or `/etc/httpd/conf/httpd.conf` 

For (CentOS/RHEL/Fedora, and often also on other distributions)


Virtual Host Configurations: These files control how Apache serves different websites (or "virtual hosts") on a single server.

`/etc/apache2/sites-available/` (Debian/Ubuntu/Mint): Contains the virtual host configuration files. These files are typically enabled by creating a symbolic link in `/etc/apache2/sites-enabled/`.

`/etc/httpd/conf.d/` (CentOS/RHEL/Fedora): Can contain virtual host configurations (often .conf files for individual websites).

`/etc/httpd/sites-available/` and `/etc/httpd/sites-enabled/` (some CentOS/RHEL/Fedora setups)


Modules Configuration: `/etc/apache2/mods-available/` and `/etc/apache2/mods-enabled/` 

(Debian/Ubuntu/Mint) or `/etc/httpd/conf.modules.d/`

(CentOS/RHEL/Fedora): Control which Apache modules are loaded.

2. Nginx (Engine X):
Main Configuration File: `/etc/nginx/nginx.conf`

Virtual Host Configurations:
`/etc/nginx/conf.d/` : This is often the primary location for site-specific configuration files. Each .conf file in this directory typically defines a virtual host.

`/etc/nginx/sites-available/` and `/etc/nginx/sites-enabled/` (less common, but sometimes used like Apache): Similar to Apache, this setup involves creating symbolic links.

Important Note: With Nginx, the include directive in nginx.conf (or other configuration files) often points to other config files or directories. This means your configuration might be split across multiple files.

- Run command:
 
```bash
sudo nano /etc/nginx/nginx.conf
```
- Locate the server block and update to fix the error mail

Sample authentication script can be found on website (http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript)

	{

        auth_http localhost/auth.php;
        pop3_capabilities "TOP" "USER";
        imap_capabilities "IMAP4rev1" "UIDPLUS";

        server {
                listen     localhost:110;
                protocol   pop3;
                proxy      on;
        }

        server {
                listen     localhost:143;
                protocol   imap;
                proxy      on;
        }
	}

- Save the `nginx.conf` file
- Test the Configuration: `sudo nginx -t`
- Restart Nginx: `sudo systemctl restart nginx`
- Check Nginx status: `sudo systemctl status nginx`
- Verify mail logs: `sudo grep -i "CTF" /var/log/mail.log /var/log/syslog /var/log/daemon.log`

```bash
/var/log/syslog:Mar  6 03:16:04 ip-10-0-1-81 cloud-init[1181]: <h2 style="text-align:center;">Flag value: CTF{web_config}</h2>
```

#### Challenge 12: Network Traffic Analysis
Someone is sending secret messages via ping packets.

- **Skills**: Network dumps, packet inspection, decoding
- **Hint**: Utilize general network analysis techniques to inspect traffic and search for concealed information.

##### Solution
- Capture Network Traffic (if not provided) `sudo tcpdump -i any icmp -w icmp_traffic.pcap`
    - Press Ctrl + C after some time to stop capturing.
- Install **tshark** `sudo apt install tshark`
- Inspect the PCAP File Use tshark or Wireshark (CLI-based analysis) to check for ICMP packets: `tshark -r icmp_traffic.pcap | grep ICMP`
- Look for Unusual Data in ICMP Payloads: `Use tshark to examine payloads`

```bash
tshark -r icmp_traffic.pcap -Y "icmp" -T fields -e data
```
If the output looks encoded, the message may be in ASCII, Base64, or another encoding.

- Extract ICMP Payloads
If you find hexadecimal data in the output, extract and decode it:

```bash
tshark -r icmp_traffic.pcap -Y "icmp" -T fields -e data > extracted_data.txt # verify 12 CTF{net_chat} CTF{net_chat} CTF{net_chat} CTF{net_chat}
```
- Then, convert hex to ASCII: `cat extracted_data.txt | xxd -r -p`

`If it’s Base64 encoded, decode it: cat extracted_data.txt | base64 -d` # option 2


## Tips for Success

1. Use `man` pages to understand command options
2. Break down complex problems into smaller steps
3. Understand command combinations using pipes
4. Review basic Linux concepts from Phase 1 Guide
5. Take notes on new commands you discover
