# Branch Naming Conventions

A consistent branch naming convention helps keep your repository organized and makes it easier to identify the purpose of each branch.

## General Guidelines

- Use **lowercase letters**.
- Separate words with hyphens (`-`).
- Keep branch names **short and descriptive**.
- Prefix branch names based on the type of work being done.

---

## Naming Format

`<prefix>/<issue-or-feature-description>`

### Common Prefixes

| Prefix         | Usage                                                                 |
|----------------|-----------------------------------------------------------------------|
| `feature`      | For new features being developed.                                     |
| `bugfix`       | For fixing specific bugs.                                             |
| `hotfix`       | For urgent fixes directly to the main branch.                         |
| `release`      | For preparing releases.                                               |
| `refactor`     | For refactoring code without adding new features or fixing bugs.      |
| `chore`        | For miscellaneous tasks like dependency updates or CI/CD changes.     |

---

## Examples

### Features
- `feature/telegram-bot-integration`
- `feature/wallet-tracking`

### Bug Fixes
- `bugfix/fix-wallet-validation`
- `bugfix/api-timeout-issue`

### Hotfixes
- `hotfix/critical-transaction-issue`

### Releases
- `release/v1.0.0`

### Refactoring
- `refactor/optimize-database-queries`
- `refactor/improve-logging`

### Chores
- `chore/update-dependencies`
- `chore/setup-ci-cd`

---

## Best Practices

1. **Link Branches to Issues**:
   - Include the issue number for better traceability (e.g., `feature/123-add-notifications`).

2. **Avoid Long Names**:
   - Keep the branch name concise but descriptive.

3. **Separate Words Clearly**:
   - Use hyphens for better readability.

4. **Use Specific Names**:
   - Avoid generic names like `feature/update` or `bugfix/fix`.

5. **Use Verb-Noun Phrases**:
   - For example, `feature/add-transaction-notifications`.

---

By following these conventions, you'll make your repository easier to navigate and collaborate on.
