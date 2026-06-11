# GitHub API Test Suite

Pytest suite for testing the GitHub REST API - authentication, repository CRUD
lifecycle with automatic cleanup fixtures, parametrized and negative tests,
mocked unit tests and async pagination checks with httpx. Runs via Docker Compose 
in a GitHub Actions pipeline with authentication and HTML reports.

**Stack:** pytest · requests · httpx · Docker · GitHub Actions

## Setup

```bash
pip install -r requirements.txt
```

Create `.env`:
```
GITHUB_TOKEN=your_personal_access_token
```

## Run

```bash
pytest                          # local
docker compose up --build      # containerized, report lands in ./reports
```

## Structure

- `conftest.py` — session-scoped authenticated session fixture
- `test_github_auth.py` — authentication checks
- `test_github_repos.py` — parametrized public repo tests
- `test_crud.py` — full create/read/update/delete lifecycle
- `test_mock.py` — unit tests with mocked HTTP (no actual network calls)
- `test_pagination.py` — concurrent async page fetches via httpx

CI runs on every push to `main` and `feature/*` branches and blocks merges on test failure.
