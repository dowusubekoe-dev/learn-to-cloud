# Introductio to Version Control (Git)

## **1. What is Version Control?**

Imagine you're writing a document (a report, a program, a website). You make changes, save it, and then later realize you messed something up. You wish you could go back to the previous version. That's where version control comes in.

**Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later.**

Think of it like a sophisticated "undo" button, but far more powerful. It allows you to:

*   **Track Changes:** See exactly *who* made *what* changes, *when*, and *why*.
*   **Revert to Previous Versions:**  Go back to an earlier state of the file or project.  This is invaluable if you make a mistake or want to experiment without breaking things permanently.
*   **Collaborate Efficiently:**  Multiple people can work on the same files simultaneously without overwriting each other's work. Version control systems help manage these parallel changes and resolve any conflicts.
*   **Branch and Merge:**  Create separate lines of development (branches) to work on new features or bug fixes without affecting the main project. Later, you can merge these changes back into the main project.
*   **Audit Trail:**  Provide a complete history of all changes, which can be helpful for debugging, understanding the evolution of a project, and meeting compliance requirements.

**Analogy:**

Think of version control like Google Docs' revision history. You can see all the changes made to a document over time and revert to any previous version. Version control systems like Git do this for *any* type of file (code, documents, images, etc.) and on a much larger scale for entire projects.

**Key Terms:**

*   **Repository (Repo):** The place where all the versions of your files and the history of changes are stored.
*   **Commit:** A snapshot of the changes you've made to the files at a specific point in time. It's like saving a version of your project.
*   **Branch:** A separate line of development.  Think of it as creating a copy of your project to work on a new feature or bug fix.
*   **Merge:**  Combining the changes from one branch into another.  For example, merging a bug fix branch back into the main project.
*   

## **2. What is a Git Repository?**

A Git repository (often called a "repo") is a storage location for all the files in your project, along with the entire history of changes to those files.

**It's like a database that tracks every modification you've made to your project over time.**

There are two main types of Git repositories:

*   **Local Repository:** This is the repository on your computer. It's where you make changes to your files, commit those changes, and experiment with branches.
*   **Remote Repository:** This is a repository hosted on a server, often on a platform like GitHub, GitLab, or Bitbucket. It's used for collaboration and backup.  It allows multiple people to work on the same project and share their changes.

**Key Functions:**

*   **Storage:** Stores all files, directories, and the complete history of the project.
*   **Change Tracking:**  Records every change made to the files, including who made the change, when, and why (through commit messages).
*   **Version Management:**  Allows you to access any previous version of the files.
*   **Collaboration:**  Enables multiple developers to work on the same project concurrently.

**Think of it this way:** Your local Git repository is like your personal workspace where you make changes. The remote repository is like a shared workspace or backup location where you can share your changes with others and ensure your work is safe.

## **3. What does it mean to clone a repository?**

Cloning a repository means creating a *local copy* of a *remote* Git repository.

**It's like downloading all the files and the entire history of a project from a remote server to your computer.**

**How it works:**

When you clone a repository, Git does the following:

1.  **Downloads all the files:**  It copies all the files and directories from the remote repository to your local machine.
2.  **Downloads the entire history:** It downloads the complete history of changes, including all commits, branches, and tags.
3.  **Sets up a connection to the remote:** It establishes a connection between your local repository and the remote repository so you can later push your changes to the remote or pull updates from it.

**Why clone a repository?**

*   **To work on a project:**  You clone a repository to get a local copy of the project's code so you can make changes, add features, or fix bugs.
*   **To contribute to an open-source project:**  You clone a repository to get the source code of an open-source project so you can contribute to its development.
*   **To create a backup:** You clone a repository to create a local backup of a project's code.
*   **To learn from a project:** You clone a repository to examine the code and learn from its structure and implementation.

**Command:**

The command to clone a repository is `git clone <repository_url>`. For example:

```bash
git clone https://github.com/dowusubekoe-dev/learn-to-cloud.git
```

This command would create a directory named `learn-to-cloud` in your current directory and download the entire contents of the remote repository into that directory.  Your local repository is now a complete, independent copy of the remote repository.

## What is Markdown?

Markdown is a lightweight markup language with plain text formatting syntax.  It's a way to format text using simple symbols that are easy to read in their raw form but can be converted into HTML (for web pages), PDFs, or other formats.

**Think of it as a simplified way to create formatted documents without using a complex word processor like Microsoft Word.**

**Key Features:**

*   **Plain Text:** Markdown files are just plain text files, so they're easy to create and edit using any text editor.
*   **Simple Syntax:**  Uses symbols like `#`, `*`, `_`, and `[]()` to indicate headings, lists, emphasis, links, and images.
*   **Human-Readable:**  The Markdown syntax is designed to be easy to read and understand, even in its raw form.
*   **Versatile:** Can be converted to HTML, PDF, or other formats using Markdown processors.

**Examples:**

*   `# Heading 1`  ->  `<h1>Heading 1</h1>` (in HTML)
*   `**Bold Text**` ->  `<strong>Bold Text</strong>` (in HTML)
*   `* Item 1` ->  `<li>Item 1</li>` (in HTML, inside a `<ul>` list)
*   `[Link to Google](https://www.google.com)` ->  `<a href="https://www.google.com">Link to Google</a>` (in HTML)

**Use Cases:**

*   **Documentation:**  Writing documentation for software projects.
*   **README Files:**  Creating README files for GitHub repositories (explaining what the project is about).
*   **Blog Posts:**  Writing blog posts or articles.
*   **Notes:**  Taking notes in a structured and formatted way.

**Why is it useful?**

Markdown is simple, portable, and easy to learn. It's ideal for creating content that needs to be formatted but doesn't require the complexity of a full-blown word processor.  It's particularly popular in the software development world because it's easily integrated with version control systems.



**In summary:**

*   **Version control:** A system for tracking changes to files over time.
*   **Markdown:** A lightweight markup language for formatting text.
*   **Git repository:** A storage location for a project's files and history.
*   **Clone:** To create a local copy of a remote Git repository.


### Resource for Git Installation
`https://git-scm.com/downloads`


### How to check the version
`git --version`


### Setting Username in Git
`git config --global user.name "<USER_NAME>"`


### Setting Email in Git
`git config --global user.email "<USER_EMAIL>"`


### Confirm Status of all Configurations
`git config --list`


### Basic Git Commands

1. **git status** :- displays the state of the working tree and changes that are currently being tracked by Git.

2. **git add** :- is used to notify Git to start keeping track of changes in certain files.

3. **git commit** :- command to invoke the stagged changes to a database in Git.

4. **git log** :- allow users to see information about previous commits.

5. **git help** :- help with getting information about all commands in Git.

6. **git add -f foldername/\\*** :- add folder with the content


## Tasks

1.  **Install VS Code:**
    *   Install the Visual Studio Code (VS Code) editor. This will be your primary programming environment.

2.  **Set up WSL (Windows Only):**
    *   **Conditional Task:** If you are using a Windows machine, proceed with this step. Mac and Linux users can skip to Task 3.
    *   Install and configure [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode). All labs and tools are designed for a Linux-based environment, and WSL provides that.
    *   Follow the instructions in this guide: "Get started using Visual Studio Code with Windows Subsystem for Linux".

3.  **Review Command Line Basics:**
    *   Study and familiarize yourself with common command-line commands. You'll be using these frequently.
    *   Use this resource: "[Command Line for Beginners](https://www.freecodecamp.org/news/command-line-for-beginners/#heading-most-common-and-useful-commands-to-use) – How to Use the Terminal Like a Pro".

4.  **Create a Lab Directory:**
    *   Open a terminal (WSL terminal on Windows, regular terminal on Mac/Linux).
    *   Use the `mkdir` command to create a new directory on your computer where you will store all labs and projects.
    *   Name the directory `learn-to-cloud`.
    *   Use the `cd` command to navigate into the newly created `learn-to-cloud` directory.

5.  **Clone the Lab Repository:**
    *   Still inside the `learn-to-cloud` directory in your terminal:
    *   Use the `git clone` command to clone the `linux-ctfs` repository locally:

        ```bash
        git clone https://github.com/learntocloud/linux-ctfs
        ```
6.  **Learn Markdown:**
    * Study the basics of Markdown. You'll be using it for documentation.
    * Use this resource: "Communicate using markdown"

7.  **Create a GitHub README:**
    * Create a README file for your GitHub profile. This is a file that describes you. This may already exists if you have previously initialised it.

8. **Edit and Push README (Using VS Code):**
    * Clone your GitHub profile's README repository to your local machine (inside or outside the l2c directory, your choice). You can find the URL for cloning on your GitHub profile page. Use a terminal.
  
        ```bash
        git clone <your_readme_repository_url>
        ```
    * Open the cloned README file in VS Code.
    * Edit the README file using Markdown:
        * Write a brief description of who you are.
        * Add links to your social media profiles (if you have them).
        * Note: Don't worry about making it too fancy.
    * Save the changes in VS Code.
    * Open the VS Code terminal (View -> Terminal or Ctrl+`).
    * Use Git commands in the VS Code terminal to stage, commit, and push your changes back to GitHub:
  
        ```bash
        git add .
        git commit -m "Update README with personal info"
        git push origin main
        ```


