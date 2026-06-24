# GIT-WORKFLOW.md

## REQUIRED RULE

For every task that changes project files, always follow this process.

## Branch Structure

```text
main                              ← main branch, always ready for deployment
 ├── feature/...                  ← new functionality
 ├── bugfix/...                   ← bug fixes
 ├── docs/...                     ← documentation
 ├── refactor/...                 ← code refactoring
 ├── test/...                     ← tests
 └── hotfix/...                   ← critical production fixes
```

* **`main`** is the only permanent branch. It must always be stable and ready for deployment.
* **Task branches** are short-lived branches created from `main`. They are merged back into `main` after the work is complete.
* **Releases** use Git tags in the `vX.Y.Z` format on the `main` branch. The continuous integration system builds a Docker image and creates a GitHub Release.

## Work Process

### 1. Before Starting Work

```bash
git checkout main
git pull origin main

# Create a task branch from main
git checkout -b <type>/<short-description>
```

### Branch Naming

Use one of these prefixes:

* `feature/` for new functionality
* `bugfix/` for bug fixes
* `docs/` for documentation
* `refactor/` for code refactoring that does not change functionality
* `test/` for adding or improving tests
* `hotfix/` for critical production fixes

Examples:

* `feature/admin-auth-oauth2`
* `docs/auth-mechanics-documentation`
* `bugfix/storage-element-wal-race-condition`

### 2. Perform the Work

* Make all changes in the task branch.
* Create intermediate commits when necessary.
* Small and low-risk changes, such as typo corrections or minor fixes, may be committed directly to `main`.

### 3. After Completing the Task, Offer to Create a Commit

Ask the user:

> The work is complete. Should I create a commit?

Use the Conventional Commits message format:

```text
<type>(<scope>): <subject>

[optional body]
```

Available commit types:

* `feat` for new functionality
* `fix` for a bug fix
* `docs` for documentation
* `style` for formatting changes
* `refactor` for code refactoring
* `test` for tests
* `chore` for maintenance work

### 4. After Creating the Commit, Offer to Merge It into `main`

Ask the user:

> The commit has been created. Choose how to merge it into `main`:
>
> **Option A: Local merge**
>
> ```bash
> git checkout main
> git merge --no-ff <branch-name>
> git push origin main
> ```
>
> **Option B: GitHub pull request**
>
> ```bash
> git push origin <branch-name>
> gh pr create --base main --fill
> ```

Do not merge the branch until the user chooses one of these options.

### 5. After the Merge, Delete the Temporary Branch

```bash
git branch -d <branch-name>
git push origin --delete <branch-name>
```

Delete the remote branch only if it was pushed to the remote repository.

### 6. Create a Release Tag

When enough functionality is ready for a release, use the following commands:

```bash
git checkout main
git pull origin main
git tag -a vX.Y.Z -m "Release vX.Y.Z"
git push origin vX.Y.Z
```

## Important Rules

1. **The `main` branch must always be ready for deployment.** Never merge broken or untested code.
2. **Keep task branches short-lived.** Merge them as soon as the work is complete and verified.
3. **Always use the Conventional Commits format.**
4. **Delete task branches after merging them.** Do not leave unused branches in the repository.
5. **Create releases with Git tags, not release branches.**
6. **Use a GitHub pull request for significant changes.** Complete a code review before merging them.
7. **Do not create commits, merge branches, push changes, delete branches, or create release tags without the user's explicit approval.**

## Example of the Complete Process

```bash
# 1. Update main
git checkout main
git pull origin main

# 2. Create a task branch
git checkout -b docs/update-readme-authentication

# 3. Make the required file changes

# 4. Create a commit after receiving user approval
git add .
git commit -m "docs(admin-module): add authentication documentation"

# 5. Merge into main after the user chooses the merge method
git checkout main
git merge --no-ff docs/update-readme-authentication
git push origin main

# 6. Delete the temporary branch
git branch -d docs/update-readme-authentication

# Delete the remote branch if it exists
git push origin --delete docs/update-readme-authentication

# 7. Create a release tag when the release is ready
git tag -a v0.2.0 -m "Release v0.2.0"
git push origin v0.2.0
```
