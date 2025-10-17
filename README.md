# GitHub Actions Hello World

This repository demonstrates a minimal Python “Hello, World!” application paired with a multi-stage GitHub Actions workflow.

## Application

- `app/main.py` exposes a simple `hello()` function and prints the greeting when executed directly.
- `tests/test_main.py` contains a single unit test that verifies the greeting text.

### Run locally

```bash
python -m app.main
```

### Run tests

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## CI/CD pipeline

The workflow in `.github/workflows/deploy.yml` performs three stages on pushes to `main` or manual dispatch:

1. `build-and-test`: Install dependencies and run the unit tests.
2. `deploy-test`: Simulated deployment to a `test` environment once the build succeeds.
3. `deploy-prod`: Promotion to `prod` after `deploy-test`, requiring an environment approval gate.

Configure the `prod` environment in GitHub with required reviewers to enforce the manual approval step. You can add environment secrets (e.g. `TEST_DEPLOY_TOKEN`, `PROD_DEPLOY_TOKEN`) if needed for real deployments.
