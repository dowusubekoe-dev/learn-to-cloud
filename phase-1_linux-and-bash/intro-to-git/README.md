# Introductio to Git

## Project Overview


## Problem Statement


## Learning and Development


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


### Challenges

- Git push command generated an error `failed to push some refs error'
- Identified that git Code URL has been set to HTTPS by default but not SSH
 

### Solution

- Run `git remote -v`
- Set a new URL for the remote `git remote set-url git@github.com:MY/REPOSITORY.git`
- Run the command `git push -u origin main`
- Refresh remote repository on GitHub

