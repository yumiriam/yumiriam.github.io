# Git Guide

Reference: [git - the simple guide](http://rogerdudler.github.com/git-guide/)

## Workflow

Your local repository consists of three "trees" maintained by git:
- The first one is your `Working Directory` which holds the actual files
- The second one is the `Index` which acts as a staging area, and finally
- The `HEAD` which points to the last commit you've made.

## Branching

- Branches are used to develop features isolated from each other.
- The `master` branch is the "default" branch when you create a repository.
- Use other branches for development and merge them back to the master branch upon completion.
- A branch is not available to others unless you push the branch to your remote repository.

## Tagging

- It's recommended to create tags for software releases.
- This is a known concept, which also exists in SVN.

## Commands

- To create a new git repository
    `git init`

- To add files to the Index (Stage)
    `git add <filename>`
    `git add *` ~ `git add --all`

- To undo:
    `git reset`

- To commit the changes:
    `git commit -m "Commit message"`

- To create a working copy of a local repository:
    `git clone /path/to/repository`

- To create a working copy of a remote repository:
    `git clone username@host:/path/to/repository`

- To send changes to your remote repository:
    `git push <remote> <local_branch>`

- To connect your repository to a remote server (not cloned):  
    `git remote add <remote> <server>`

### Branches

- To create a new branch:
    `git checkout -b <branch>`

- To switch branches:
    `git checkout <branch>`

- To delete the branch:
    `git branch -d <branch>`

### Update & Merge

- To update your local repository to the newest commit:
    `git pull`

- To merge another branch into your active branch:
    `git merge <branch>`

- After merging conflicts manually, you need to mark them as merged:
    `git add <filename>`

- Before mergin changes, you can also preview them by using:
    `git diff <source_branch> <target_branch>`

### Tags

- To create a new tag:
    `git tag <tagname> <commit_id>[0:9]`

### Log

- To view repository history:
    `git log`

- To see only the commits of a certain author:
    `git log --author=<author>`

To see a very compressed log where each commit is one line:
    `git log --pretty=oneline`

- To see an ASCII art tree of all the branches:
    `git log --graph --oneline --decorate --all`

- To see which files have changed:
    `git log --name-status`

### Local Changes

- To replace local changes (working tree) with the last content in HEAD:
    `git checkout -- <filename>`

    - Changes already added to the index, as well as new files, will be kept

- To drop all your local changes and commits, fetch the latest history from the server and point your local master branch at it:
    `git fetch origin`
    `git reset --hard origin/master`


## GitK

    `gitk --all`

