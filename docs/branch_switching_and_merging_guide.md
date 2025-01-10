# Branch Switching and Merging Guide

Properly switching and merging branches ensures that your code stays up to date and conflicts are minimized. This guide outlines best practices for merging and updating branches during development.

---

## Branch Workflow Overview

1. **Base Branch**: The `main` or `master` branch is the production-ready code.
2. **Development Branch**: Use the `dev` branch for integrating features and bug fixes.
3. **Feature Branches**: Individual branches for specific features or bug fixes (`feature/<description>` or `bugfix/<description>`).

---

## Steps for Switching and Merging

### 1. **Starting a Feature Branch**
- Always branch off from the latest `dev` branch:
  ```bash
  git checkout dev
  git pull origin dev
  git checkout -b feature/<description>
  ```

### 2. **Regularly Update Feature Branch**
- To avoid conflicts, keep your feature branch updated with `dev`:
  ```bash
  git checkout dev
  git pull origin dev
  git checkout feature/<description>
  git merge dev
  ```
- Resolve any merge conflicts immediately.

### 3. **Completing a Feature**
- Ensure your feature branch is up to date before merging into `dev`:
  ```bash
  git checkout dev
  git pull origin dev
  git checkout feature/<description>
  git merge dev
  ```
- Test thoroughly to ensure functionality.

### 4. **Merging Feature to Dev**
- Merge your completed feature branch into `dev`:
  ```bash
  git checkout dev
  git merge feature/<description>
  ```
- Push changes to the remote repository:
  ```bash
  git push origin dev
  ```

### 5. **Cleaning Up**
- Delete the feature branch after merging:
  ```bash
  git branch -d feature/<description>
  git push origin --delete feature/<description>
  ```

---

## Additional Scenarios

### a. **Hotfixes to Main**
- If a critical fix is required:
  1. Create a hotfix branch from `main`:
     ```bash
     git checkout main
     git pull origin main
     git checkout -b hotfix/<description>
     ```
  2. Merge the hotfix into `main` and `dev`:
     ```bash
     git checkout main
     git merge hotfix/<description>
     git push origin main

     git checkout dev
     git merge hotfix/<description>
     git push origin dev
     ```

### b. **Returning to a Feature**
- If you pause work on a feature and need to continue later:
  1. Ensure `dev` is up to date:
     ```bash
     git checkout dev
     git pull origin dev
     ```
  2. Merge `dev` into the feature branch:
     ```bash
     git checkout feature/<description>
     git merge dev
     ```
  3. Resolve any conflicts and continue working.

---

## Best Practices

1. **Always Pull Before Starting Work**:
   - Ensure your branch starts with the latest changes.

2. **Commit Frequently**:
   - Make small, descriptive commits to track progress.

3. **Test Before Merging**:
   - Run tests locally to confirm your changes work as expected.

4. **Communicate Merge Conflicts**:
   - If you encounter conflicts, notify team members to avoid duplication of effort.

5. **Use Pull Requests (PRs)**:
   - For collaborative projects, submit a PR and request a review before merging.

---

By following these steps, you ensure smooth collaboration and maintain a clean repository history. Let me know if you need further clarification!
