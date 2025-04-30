# Linux Bash Basics

This document provides an overview of essential Linux Bash commands and concepts that are foundational for working in a cloud environment.

## Foundational Commands

Familiarize yourself with the following essential commands:

- **`pwd`**: Prints the current working directory, showing your current location in the filesystem.
- **`cd`**: Changes the directory, allowing you to navigate between folders.
- **`ls`**: Lists the contents of a directory.

## Challenge 1: Hidden Files

Learn how to find hidden files using these commands:

- **`ls -a`**: Lists all files, including hidden ones (those starting with a dot).
- **`ls -la`**: Provides a detailed listing of all files, including hidden ones.
- **`find . -name ".*"`**: Searches for hidden files in the current directory.

### Search Commands

```bash
# Find all files in current directory and subdirectories
find . -type f

# Find files containing specific text
grep -r "CTF{" .

# Find hidden files (they start with .)
ls -la
```

### Navigation Commands

```bash
# Show current directory
pwd

# List directory contents with details
ls -l

# Change to home directory
cd ~

# Move up one directory
cd ..
```

### File Reading Commands

```bash
# View file contents
cat filename

# View file contents page by page
less filename

# View first few lines of file
head filename

# View last few lines of file
tail filename
```

### System Information

```bash
# Show system processes
ps aux

# Show current user
whoami

# Show system information
uname -a

# Show environment variables
env
```

### File Permissions and Ownership
```bash
# Show file permissions
ls -l filename

# Change file permissions
chmod permissions filename

# Change file ownership
chown user:group filename
```
---

## Challenge 2: File Searching

Master the following commands for searching files:

- **`find /path -name "pattern"`**: Searches for files by name in the specified path.
- **`find /path -type f`**: Searches for regular files in the specified path.
- **`locate filename`**: Quickly searches for files using a pre-built database.
- **`grep -r "text" /path`**: Recursively searches for specific text within files in the specified path.
- **`find /path/to/search -name "*secret*"`**: Basic find command - search for files with "secret" in the name
- **`find /path/to/search -iname "*secret*"`**: Case-insensitive search for files with "secret" in the name
- **`find /path/to/search -type f -name "*secret*"`**: Search only files (not directories)
- **`find . -name "*secret*"`**: Search in current directory and subdirectories
- **`find /home/ctf_user -type f -name "*secret*"`**: Example for Challenge 2 (searching in /home/ctf_user for "secret")

---

## Challenge 3: File Size Analysis

Use these commands to analyze file sizes:

- **`ls -lh`**: Lists files with human-readable sizes.
- **`du -h`**: Displays disk usage in a human-readable format.
- **`sort -h`**: Sorts files by human-readable sizes.
- **`find /path -type f -size +1M`**: Finds files larger than 1MB.

## Challenge 4: User Investigation

Commands for user management include:

- **`id username`**: Displays the user ID and groups for a specified user.
- **`cat /etc/passwd`**: Views user account information.
- **`getent passwd uid`**: Retrieves user information by UID.
- **`ls -l /home/`**: Lists home directories for users.

## Challenge 5: Permission Analysis

Work with file permissions using these commands:

- **`ls -l`**: Views file permissions in a detailed format.
- **`stat filename`**: Provides detailed information about a file.
- **`find / -perm 777`**: Finds files with specific permissions.
- **`chmod`**: Changes file permissions.

## Challenge 6: Network Services

Investigate network services with the following commands:

- **`netstat -tuln`**: Lists listening ports and their associated services.
- **`ss -tuln`**: A modern alternative to `netstat` for listing sockets.
- **`lsof -i`**: Lists open network files.
- **`curl localhost:port`**: Tests an HTTP service on a specified port.
- **`nc -zv host port`**: Tests a TCP connection to a specified host and port.

## Challenge 7: Encoding/Decoding

Text processing commands include:

- **`base64`**: Encodes or decodes data in base64 format.
- **`echo -n "text"`**: Outputs text without a trailing newline.
- **`|`**: The pipe operator, used for chaining commands together.

## Challenge 8: SSH Configuration

Commands related to SSH configuration:

- **`ls -la ~/.ssh/`**: Lists the contents of the SSH directory.
- **`find ~/.ssh -type f`**: Finds SSH-related files.
- **`chmod 600`**: Sets the correct permissions for SSH keys.
- **`ssh-keygen`**: Generates SSH keys for secure access.

## General Tips

1. Combine commands for efficiency.
2. Navigate effectively:
   - Use tab completion for file and directory names.
   - Use `cd -` to return to the previous directory.
   - Use `cd ..` to move up one level in the directory structure.
3. Debug commands:
   - Add `-v` or `--verbose` for more detailed output.
   - Check command syntax using `man` (manual).
   - Use `which command` to verify the location of a command.

By mastering these commands and concepts, you will build a strong foundation for working with Linux in cloud environments.

For more detailed information, visit my Medium blog post [Linux Basics](https://github.com/dowusubekoe-dev/blog-post/tree/main/1-Linux).
