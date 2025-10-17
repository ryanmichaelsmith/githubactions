# GitHub Actions Hello World

This repository demonstrates a minimal Python “Hello, World!” application paired with a GitHub Actions-based deployment pipeline.

## Application

- `app/main.py` exposes a simple `hello()` function and prints the greeting when executed directly.
- `app.get_version()` attempts to read the installed package version and falls back to `0.0.0` when run locally.
- `tests/test_main.py` verifies both behaviours.

### Run locally

```bash
poetry install
poetry run python -m app.main
```

### Run tests

```bash
poetry run pytest
```

## Versioning

Project metadata and dependency management are handled by Poetry (`pyproject.toml`). Automated workflows use `poetry version` to manage semantic version numbers:

- Manual deployments to the **test** environment bump the patch/build version.
- Manual deployments to **prod** bump the minor version and create a matching `v<version>` tag.

## GitHub Actions workflows

- `.github/workflows/ci.yml` runs on pushes to `main` and on pull requests. It installs dependencies via Poetry and runs the unit tests.
- `.github/workflows/deploy-test.yml` is triggered manually (`workflow_dispatch`). It bumps the patch version, runs the simulated test deployment, commits the version change, and pushes it back to the selected branch.
- `.github/workflows/deploy-prod.yml` is also manual and targets the `prod` environment. After approval, it bumps the minor version, runs the simulated production deployment, commits, tags the release, and pushes both the branch and tag.

Configure the `prod` environment in GitHub with required reviewers to enforce the approval gate before production deployments. Add environment secrets (e.g., `TEST_DEPLOY_TOKEN`, `PROD_DEPLOY_TOKEN`) as needed for real deployments.
