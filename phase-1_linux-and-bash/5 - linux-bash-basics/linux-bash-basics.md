# Linux Bash Basics

Linux and Bash are core skills for cloud engineering. You use them to connect to servers, inspect files, troubleshoot services, read logs, install tools, manage permissions, debug networks, and automate repeated work.

## 1. Getting Started with the Basics

### What to Know

The command line lets you control a Linux system by typing commands. In cloud engineering, you will often use the CLI when working with virtual machines, containers, CI/CD systems, and remote servers.

The Linux filesystem starts at `/`, called the root directory. Everything lives somewhere under `/`.

Common directories:

- `/home`: user home directories.
- `/root`: home directory for the root/admin user.
- `/etc`: system configuration files.
- `/var`: changing files such as logs, caches, and application data.
- `/tmp`: temporary files.
- `/usr`: installed programs and shared resources.
- `/bin` and `/sbin`: essential system commands.
- `/opt`: optional third-party software.

### Key Commands

- `pwd`: print the current working directory.
- `cd`: change directory.
- `ls`: list files and directories.
- `whoami`: show the current logged-in user.
- `man`: open a command's manual page.

### Examples

```bash
# Show your current location
pwd

# Go to your home directory
cd ~

# Move up one directory
cd ..

# List files
ls

# List files with details
ls -l

# List hidden files too
ls -la

# Show current user
whoami

# Read the manual for ls
man ls
```

### Mini Project: Filesystem Explorer

Create a short map of your Linux system.

1. Run `pwd`, `whoami`, and `ls -la`.
2. Visit `/`, `/home`, `/etc`, `/var`, and `/tmp`.
3. For each directory, write one sentence explaining what it appears to contain.
4. Use `man ls` to find what the `-h` option does.

Expected outcome: you can navigate confidently and explain where common system files live.

## 2. Text Manipulation

### What to Know

Cloud engineers spend a lot of time reading logs, configuration files, command output, and deployment files. Text tools help you inspect, filter, and transform that information quickly.

Pipes and redirects are especially important:

- `|`: send output from one command into another command.
- `>`: write output to a file, replacing existing content.
- `>>`: append output to a file.
- `<`: use a file as command input.

### Key Commands

- `cat`: print a file's contents.
- `head`: show the first lines of a file.
- `tail`: show the last lines of a file.
- `grep`: search text using patterns.
- `sed`: edit or transform text streams.

### Examples

```bash
# Print a file
cat app.log

# Show first 10 lines
head app.log

# Show last 20 lines
tail -n 20 app.log

# Follow a log file as it changes
tail -f app.log

# Find lines containing ERROR
grep "ERROR" app.log

# Case-insensitive search
grep -i "error" app.log

# Search recursively in a directory
grep -r "database" .

# Replace text in command output
sed 's/error/ERROR/g' app.log

# Save command output to a file
grep "ERROR" app.log > errors.txt

# Append output to a file
grep "WARN" app.log >> errors.txt

# Count matching lines
grep "ERROR" app.log | wc -l
```

### Mini Project: Log Filter

Create a small file called `sample.log` with INFO, WARN, and ERROR lines. Then:

1. Show the first 5 lines with `head`.
2. Show the last 5 lines with `tail`.
3. Find all ERROR lines with `grep`.
4. Save ERROR lines to `errors.txt`.
5. Use `sed` to replace `WARN` with `WARNING`.

Expected outcome: you can inspect and filter logs like you would during troubleshooting.

## 3. Analyzing and Managing Networks

### What to Know

Networking commands help you understand IP addresses, routes, DNS records, and connectivity. This matters in cloud work because applications often fail due to DNS issues, firewall rules, routing problems, or incorrect network configuration.

Modern Linux systems usually prefer `ip` over older tools like `ifconfig`.

### Key Commands

- `ip`: view and manage network interfaces, IP addresses, and routes.
- `ifconfig`: older command for network interface information.
- `iwconfig`: view wireless network interface settings.
- `dig`: query DNS records.
- DNS config files: commonly `/etc/resolv.conf` and system resolver settings.

### Examples

```bash
# Show IP addresses
ip address

# Shorter version
ip a

# Show routing table
ip route

# Older interface command, if installed
ifconfig

# Show wireless interface information, if available
iwconfig

# Query DNS A record
dig example.com

# Query a specific record type
dig example.com MX

# Query using a specific DNS server
dig @8.8.8.8 example.com

# View resolver configuration
cat /etc/resolv.conf
```

### Mini Project: Network Snapshot

Create a file called `network-report.txt` containing:

1. Your machine's IP information from `ip a`.
2. Your default route from `ip route`.
3. DNS results for `example.com` using `dig`.
4. The DNS resolver configuration from `/etc/resolv.conf`.

Example:

```bash
ip a > network-report.txt
ip route >> network-report.txt
dig example.com >> network-report.txt
cat /etc/resolv.conf >> network-report.txt
```

Expected outcome: you can collect useful network troubleshooting evidence.

## 4. Adding and Removing Software

### What to Know

Package managers install, update, search, and remove software. On Ubuntu and Debian-based systems, the common package manager is `apt`.

Cloud engineers use package managers to install CLIs, monitoring tools, web servers, language runtimes, and troubleshooting utilities.

### Key Commands

- `apt update`: refresh package lists.
- `apt upgrade`: upgrade installed packages.
- `apt search`: search for packages.
- `apt show`: show package details.
- `apt install`: install software.
- `apt remove`: remove software.
- `apt autoremove`: remove unused dependencies.

### Examples

```bash
# Refresh package information
sudo apt update

# Search for a package
apt search nginx

# Show package details
apt show nginx

# Install a package
sudo apt install nginx

# Remove a package
sudo apt remove nginx

# Remove unused dependencies
sudo apt autoremove
```

### Mini Project: Install a Troubleshooting Tool

Use `apt` to explore and install a safe CLI tool.

1. Run `sudo apt update`.
2. Search for `tree`.
3. Install `tree`.
4. Run `tree` in a small directory.
5. Remove `tree` if you no longer need it.

Expected outcome: you understand the install, verify, and remove lifecycle for Linux packages.

## 5. Controlling File and Directory Permissions

### What to Know

Linux permissions control who can read, write, or execute files and directories. This is critical for security, SSH keys, scripts, application files, and cloud server hardening.

Permission groups:

- User: the file owner.
- Group: users in the file's group.
- Others: everyone else.

Permission types:

- `r`: read.
- `w`: write.
- `x`: execute.

Example from `ls -l`:

```text
-rwxr-x--- 1 ubuntu ubuntu 120 script.sh
```

Meaning:

- Owner can read, write, and execute.
- Group can read and execute.
- Others have no access.

### Key Commands

- `ls -l`: view permissions.
- `chmod`: change permissions.
- `chown`: change ownership.
- `chgrp`: change group ownership.
- `stat`: view detailed file metadata.

### Examples

```bash
# View permissions
ls -l script.sh

# Add execute permission for the owner
chmod u+x script.sh

# Set permissions using numbers
chmod 755 script.sh

# Private SSH key style permissions
chmod 600 id_rsa

# Change owner and group
sudo chown ubuntu:ubuntu app.log

# View detailed metadata
stat app.log
```

Common numeric permissions:

- `600`: owner read/write only.
- `644`: owner read/write, others read.
- `700`: owner full access only.
- `755`: owner full access, others read/execute.

### Mini Project: Secure a Script

1. Create `hello.sh`.
2. Add a command that prints `Hello from Bash`.
3. Check its permissions with `ls -l`.
4. Try to run it with `./hello.sh`.
5. Add execute permission with `chmod u+x hello.sh`.
6. Run it again.
7. Change it to private owner-only access using `chmod 700 hello.sh`.

Expected outcome: you understand how permissions affect script execution.

## 6. Process Management

### What to Know

A process is a running program. Cloud engineers inspect processes when a server is slow, an application is stuck, a port is busy, or a service needs to be stopped.

Each process has a PID, which is its process ID.

### Key Commands

- `ps`: show running processes.
- `top`: live process viewer.
- `kill`: send a signal to a process.
- `nice`: start a process with a scheduling priority.
- `renice`: change priority of a running process.

### Examples

```bash
# Show processes for current shell
ps

# Show all processes in detail
ps aux

# Find a process by name
ps aux | grep nginx

# Live process view
top

# Stop a process by PID
kill 1234

# Force stop a process by PID
kill -9 1234

# Start a command with lower priority
nice -n 10 long-running-command

# Change priority of a running process
renice 10 -p 1234
```

### Mini Project: Process Detective

1. Run `sleep 300` in one terminal.
2. Open another terminal.
3. Find the `sleep` process using `ps aux | grep sleep`.
4. Note its PID.
5. Stop it with `kill PID`.
6. Confirm it stopped.

Expected outcome: you can identify and stop a running process.

## 7. Managing User Environment Variables

### What to Know

Environment variables store configuration values used by the shell and applications. They are common in cloud systems because they let you configure apps without hardcoding values.

Common variables:

- `PATH`: directories where the shell looks for commands.
- `HOME`: current user's home directory.
- `USER`: current username.
- `SHELL`: current shell path.

Shell startup files such as `~/.bashrc` can define variables or aliases every time a new shell starts.

### Key Commands

- `env`: list environment variables.
- `echo $VARIABLE`: print a variable.
- `export`: create or expose a variable to child processes.
- `source`: reload a shell config file.
- `which`: show where a command is located.

### Examples

```bash
# Show all environment variables
env

# Print home directory
echo $HOME

# Print command search path
echo $PATH

# Create a variable for the current shell
APP_ENV=dev

# Export a variable for child processes
export APP_ENV=dev

# Add a custom bin directory to PATH
export PATH="$HOME/bin:$PATH"

# Reload bash configuration
source ~/.bashrc

# Find command location
which bash
```

### Mini Project: Configure a Dev Environment

1. Create an environment variable called `APP_ENV` with value `dev`.
2. Print it with `echo $APP_ENV`.
3. Add `export APP_ENV=dev` to `~/.bashrc`.
4. Reload with `source ~/.bashrc`.
5. Open a new terminal and confirm the variable still exists.

Expected outcome: you understand temporary and persistent environment variables.

## 8. Bash Scripting

### What to Know

Bash scripting lets you save commands in a file and run them as a repeatable automation. Scripts are useful for backups, health checks, deployments, log cleanup, and server setup.

A Bash script usually starts with a shebang:

```bash
#!/bin/bash
```

### Key Concepts

- Variables: store values.
- Arguments: accept input from the command line.
- Conditionals: make decisions.
- Loops: repeat actions.
- Exit codes: tell whether a command succeeded or failed.

### Examples

```bash
#!/bin/bash

name="Cloud Engineer"
echo "Hello, $name"
```

```bash
#!/bin/bash

echo "First argument: $1"
echo "Second argument: $2"
```

```bash
#!/bin/bash

if [ -f "$1" ]; then
    echo "File exists: $1"
else
    echo "File not found: $1"
fi
```

```bash
#!/bin/bash

for file in *.log; do
    echo "Found log file: $file"
done
```

Run a script:

```bash
chmod u+x script.sh
./script.sh
```

### Mini Project: Server Health Check Script

Create `health-check.sh` that prints:

1. Current date.
2. Current user.
3. Disk usage with `df -h`.
4. Memory usage with `free -h`.
5. Top running processes with `ps aux | head`.

Starter:

```bash
#!/bin/bash

echo "Health check started at: $(date)"
echo "Running as: $(whoami)"

echo "Disk usage:"
df -h

echo "Memory usage:"
free -h

echo "Process snapshot:"
ps aux | head
```

Expected outcome: you can automate a basic troubleshooting report.

## 9. Compressing and Archiving

### What to Know

Archiving combines files into one file. Compression reduces file size. Cloud engineers use archives for logs, backups, deployment bundles, and transferring files between systems.

Common tools:

- `tar`: create and extract archive files.
- `gzip`: compress files using `.gz`.
- `bzip2`: compress files using `.bz2`.

Common `tar` options:

- `c`: create an archive.
- `x`: extract an archive.
- `t`: list archive contents.
- `v`: verbose output.
- `f`: file name.
- `z`: use gzip.
- `j`: use bzip2.

### Examples

```bash
# Create a tar archive
tar -cvf logs.tar logs/

# List archive contents
tar -tvf logs.tar

# Extract a tar archive
tar -xvf logs.tar

# Create gzip-compressed tar archive
tar -czvf logs.tar.gz logs/

# Extract gzip-compressed tar archive
tar -xzvf logs.tar.gz

# Create bzip2-compressed tar archive
tar -cjvf logs.tar.bz2 logs/

# Extract bzip2-compressed tar archive
tar -xjvf logs.tar.bz2

# Compress a single file
gzip app.log

# Decompress a gzip file
gunzip app.log.gz
```

### Mini Project: Log Backup Archive

1. Create a directory called `logs`.
2. Add three fake log files inside it.
3. Create a compressed archive called `logs-backup.tar.gz`.
4. List the archive contents.
5. Extract it into a new directory called `restore-test`.
6. Confirm the files were restored.

Example:

```bash
mkdir logs
echo "INFO app started" > logs/app.log
echo "WARN disk usage high" > logs/system.log
echo "ERROR database timeout" > logs/db.log
tar -czvf logs-backup.tar.gz logs/
tar -tvf logs-backup.tar.gz
mkdir restore-test
tar -xzvf logs-backup.tar.gz -C restore-test
ls -la restore-test/logs
```

Expected outcome: you can package and restore files like logs or backups.

## Final Practice Project: Linux Troubleshooting Bundle

Create a script called `troubleshooting-bundle.sh` that:

1. Creates a directory called `linux-report`.
2. Saves current user and date to `linux-report/system.txt`.
3. Saves disk usage to `linux-report/disk.txt`.
4. Saves process information to `linux-report/processes.txt`.
5. Saves network information to `linux-report/network.txt`.
6. Compresses the directory into `linux-report.tar.gz`.

This combines navigation, redirects, text files, processes, networking, scripting, and archiving into one realistic cloud engineering task.

## Linux CTF Challenge

1.

