# Lab 03: Git and GitHub
This repository documents my practice with 
local Git, GitHub, branches, and pull requests.

## README Responses

### 1.1 After initialization
```text
ls -la
total 0
drwxr-xr-x   3 jamienale  staff   96 Sep  3 10:36 .
drwxr-xr-x  10 jamienale  staff  320 Sep  3 10:35 ..
drwxr-xr-x   9 jamienale  staff  288 Sep  3 10:36 .git
```

### 1.2 First git status
```text
(base) jamienale@Jamies-MacBook-Air lab03-exercises % git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	README.md

nothing added to commit but untracked files present (use "git add" to track)

```

### 1.3 After the first commit
```text
(base) jamienale@Jamies-MacBook-Air lab03-exercises % git status
On branch main
nothing to commit, working tree clean
```
### 1.4 git log
```text
(base) jamienale@Jamies-MacBook-Air lab03-exercises % git log --oneline
1155e5a (HEAD -> main) Create lab README

```

### 1.5 git diff


Paste the `git status` and `git diff` commands and their output.
```text
(base) jamienale@Jamies-MacBook-Air lab03-exercises % git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

```text
(base) jamienale@Jamies-MacBook-Air lab03-exercises % git diff
diff --git a/README.md b/README.md
index e6e4885..e9c5167 100644
--- a/README.md
+++ b/README.md
@@ -1,4 +1,6 @@
 # Lab 03: Git and GitHub
+This repository documents my practice with 
+local Git, GitHub, branches, and pull requests.
 
 ## README Responses
 
@@ -27,7 +29,11 @@ nothing added to commit but untracked files present (use "git add" to track)
 ```
 
 ### 1.3 After the first commit
+```text
+(base) jamienale@Jamies-MacBook-Air lab03-exercises % git log --oneline
+1155e5a (HEAD -> main) Create lab README
 
+```
 ### 1.4 git log
 
 ### 1.5 git diff

```
```


How does this `git status` differ from the one in **1.2**?

### 1.6 Git command reflections

In one or two sentences each, what does each command do?

- `git init`
#Initulize working branch
- `git status`
#Shows what files are staged to commit
- `git add`
Moves files into a staging area to commit
- `git commit`
#Snapshot of the current state of files that can now be merged or rebased (if no conflict exists)
- `git log`
#Shows the time line of changes of tree and their hash code
- `git diff`
#Shows the changes to files
### 1.7 Repository link

### 1.8 Comparing approaches

In your own words:

- How does the nested-loop approach check for a duplicate?
#The nested-loop approach is less efficent but easy to read and doesn't rely on implementation of other structures. 
#The nested-loop iterates one idex at a time and compares it to the rest of the items in the array. 
#O(n^2)
- How does the set-based approach check for a duplicate?
#Set based approach relys on the inherited properties of the data structure. Only unique items may be added to a set.
#By comparing the size (or length) of the set to the original array, we can tell if there are duplicates.
#O(n)
- What is the runtime and memory trade-off of each?
#The set approach is more efficent, especially on large data. 
#The set approach does rely on inheritance. Higher level can be harder to read and maintane. 
#The set approach is more scalable. 

### 1.9 Pull request merge options

In your own words, what does each GitHub merge option do?

- Create a merge commit
#git merge will create a cycle in the main tree implementing the new code in a way that maintans direction of work.
- Squash and merge
#Squash merge will create a single commit pointer. Then Merging it with main. Head pointer to the new commit.
- Rebase and merge
#Rebase does not create a cycle in the tree. If there are no conflicts, or resolved conflicts, the main point will point to
#rebased head creating a main "trunk". 