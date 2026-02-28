# Linux Shell Script and Command Line for Beginners

A **bash script** is a file containing a sequence of commands that are executed by the bash program line by line.

## Advantages of Bash Scripting

- Automation
- Portabibilty
- Flexibility
- Accessibility
- Integration
- Debugging

## Basic Shell Commands

You can always refer to a commands manual with the man command.

You enter any command after the **$** sign. Generally, commands follow this syntax:

```
command [OPTION] arguments
```

1. Determine Shell type

```bash
$ ps

# Display
PID TTY          TIME CMD
 739084 pts/5    00:00:00 bash
1174369 pts/5    00:00:00 ps
```

2. Find todays date

```bash
$ date

# Display
Mon Feb 16 09:07:10 EST 2026
```

3. Display current directory

```bash
$ pwd

# Display
/home/dev-dowusubekoe
```

4. List content of current directory

```bash
$ ls

# Display
Desktop    Downloads  Pictures  Templates  bin              docker.log   lib         my-workspace  snap    venvs
Documents  Music      Public    Videos     cleanup_backups  dockerd.log  mssql-deps  scripts       status
```

5. Print a string of text/value of a variable to the terminal

```bash
$ echo "Hello bash"

# Display
Hello bash
```

6. Reading the user input and storing it in a variable

```bash
#!/bin/bash

echo "What's your name?"
read entered_name
echo -e "\nWelcome to bash tutorial" $entered_name
```

7. Reading from a file

```bash
while read line
do
    echo $line
done < input.txt
```

8. Command line arguments. In a **script** or **function**.

- $1 denotes the initial argument passed.
- $2 denotes the second argument passed, and so forth

```bash
$ echo "Hello, $1!"
```

```bash
#!/bin/bash
echo "Hello, $1!"
```

9. Append text to a file

```bash
$ echo "More text." >> output.txt
```

10. Redirect output

```bash
$ ls > files.txt
```

**Basic Bash commands (echo, read, etc.)**

- **cd**: Change the directory to a different location.
- **ls**: List the contents of the current directory.
- **mkdir**: Create a new directory.
- **touch**: Create a new file.
- **rm**: Remove a file or directory.
- **cp**: Copy a file or directory.
- **mv**: Move or rename a file or directory.
- **echo**: Print text to the terminal.
- **cat**: Concatenate and print the contents of a file.
- **grep**: Search for a pattern in a file.
- **chmod**: Change the permissions of a file or directory.
- **sudo**: Run a command with administrative privileges.
- **df**: Display the amount of disk space available.
- **history**: Show a list of previously executed commands.
- **ps**: Display information about running processes.



## How to Create and Execute Bash script

By naming convention, bash scripts end with `.sh.` However, bash scripts can run perfectly fine without the `sh` extension.
Bash scripts start with a `shebang`. Shebang is a combination of `bash #` and `bang !` followed by the bash shell path.

Example of the shebang statement is shown below.

```
#!/bin/bash

```
To find the bash shell path, use the command:

```bash
$ which bash

```
**Creating First Bash Script**

- Create a file using the correct naming convention. E.g. `vi run_all.sh`
- Enter the following commands

```bash
  1 #!/bin/bash
  2 echo "Today is " `date`
  3
  4 echo -e "\nenter the path to directory"
  5 read the_path
  6
  7 echo -e "\n you path has the following files and folders: "
  8 ls $the_path
```
**Explanation**

- Line #1: The shebang `(#!/bin/bash)` points toward the bash shell path.
- Line #2: The echo command is displaying the current date and time on the terminal. Note that the date is in backticks.
- Line #4: We want the user to enter a valid path.
- Line #5: The read command reads the input and stores it in the variable the_path.
- Line #8: The ls command takes the variable with the stored path and displays the current files and folders.

**Executing the bash script**

To make the script executable, assign execution rights to your user using this command:

```bash
$ chmod u+x run_all.sh
```
- **`chmod`** modifies the ownership of a file for the current user :u.
- **`+x`** adds the execution rights to the current user. This means that the user who is the owner can now run the script.
- **`run_all.sh`** is the file we wish to run.

The script can be run using any of the following commands:

```bash
$ sh run_all.sh

# OR

$ bash run_all.sh

# OR

$ ./run_all.sh

```

**Variables & Data Types**

Variables let you store data. However, there are no data types in **Bash**. A **variable** can be set as:

```bash
# Assign value directly
$ country=Pakistan

# OR

# Assign the value based on the output from a program
$ same_country=$country

# To access the variable value, append $ to the variable name
$ coutry=Pakistan
$ echo $country # Pakistan

$ new_country = $country
$ echo $new_country

```

### Glossary

1. A **shell** refers to a program that provides a command-line interface for interacting with an operating system. **Bash** (Bourn-Again-SHell) is one of the most commonly used **UNIX/Linux** shells.
2. A **variable** is used in storing data and it can also be used to **read**, **access**, and **manipulate** data throughout a script.
3. 

