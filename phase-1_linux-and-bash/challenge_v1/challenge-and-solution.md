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

## Tips for Success

1. Use `man` pages to understand command options
2. Break down complex problems into smaller steps
3. Understand command combinations using pipes
4. Review basic Linux concepts from Phase 1 Guide
5. Take notes on new commands you discover

## Author

- LinkedIn: [rishabkumar7](https://linkedin.com/in/rishabkumar7)
- X/Twitter: [@rishabincloud](https://x.com/rishabincloud)

## [License](LICENSE)
