<!-- Copilot agent instructions for this repository -->
# Copilot agent instructions — OctoFit Tracker workshop

This file gives targeted, actionable context for AI coding agents working in this repository.

1) Big picture
- **Two app layers**: a Django REST backend and a React frontend under `octofit-tracker/backend` and `octofit-tracker/frontend` respectively. The backend uses Django (manage.py) and expects a Python `venv` at `octofit-tracker/backend/venv`. The frontend is a typical React app (uses `react-scripts`) in `octofit-tracker/frontend`.
- **Run ports**: Django server on `0.0.0.0:8000`, React dev server on `3000`. MongoDB is expected on port `27017` if used locally.

2) Important files & conventions (use these as anchors)
- `README.md` and `docs/octofit_story.md`: project goals and workshop context — use them to align feature naming and UX language.
- `.vscode/launch.json`: contains the intended debug/run configs. Backend launch uses `octofit-tracker/backend/manage.py runserver 0.0.0.0:8000` and points to `octofit-tracker/backend/venv/bin/python`.
- `octofit-tracker/backend/requirements.txt`: install here when working on Python dependencies (create venv at `octofit-tracker/backend/venv`).

3) How to run and debug (explicit commands)
- Create the Python venv (if missing):
```
python3 -m venv octofit-tracker/backend/venv
source octofit-tracker/backend/venv/bin/activate
pip install -r octofit-tracker/backend/requirements.txt
```
- Start backend (Django):
```
python octofit-tracker/backend/manage.py runserver 0.0.0.0:8000
```
- Start frontend (React):
```
cd octofit-tracker/frontend && npm install && npm start
```
Note: workshop workspace is typically developed in GitHub Codespaces — ensure Copilot extensions are enabled.

4) Project-specific patterns and expectations
- Prefer Django ORM for DB work (even if MongoDB is used through `djongo`); migrations and models follow standard Django patterns — locate models under the backend app folders.
- Dev environment variables and venv paths are explicit in `.vscode/launch.json`; follow these exact paths when creating debug runs.
- Keep UI and API names aligned with wording in `docs/octofit_story.md` (e.g., "Activity logging", "Team management", "Leaderboard").

5) Branching, commits and PR guidance for agents
- Branch name pattern: `feature/<short-desc>` or `fix/<short-desc>`. Example: `feature/update-copilot-instructions`.
- Commit message style: short imperative subject, optional body. Example: `docs: add copilot agent instructions (guidance + run commands)`.

6) What to change (and what to avoid)
- Update: documentation, small scaffolding, and tests that match existing structure. Use the existing `octofit-tracker` layout — do not move top-level folders.
- Avoid: changing globally-installed toolchains or assuming different port mappings than `8000`/`3000`/`27017`.

7) Examples agents should follow
- When adding a Django view, add a serializer and a corresponding URL entry in the same PR. Place tests under the backend app `tests` module.
- When adding a React page, wire the API call to `/api/...` endpoints and register the route in the frontend router.

8) Quick prompts for Copilot agent mode
- "Generate a Django serializer and view for an Activity model placed in `octofit-tracker/backend/<app>/models.py`. Add a URL under `<app>/urls.py` and a simple unit test in `<app>/tests/test_activity.py`."
- "Create a React component `ActivityLog` in `octofit-tracker/frontend/src/components/` that fetches `/api/activities/` and lists items." 

9) Where to look for more context
- Use `README.md` and `docs/octofit_story.md` for product requirements and naming conventions.
- Refer to `.vscode/launch.json` for exact run/debug paths and environment expectations.

If any of the file paths or run commands above are out of date, please propose a minimal PR that only updates the run/debug instructions and `README.md` first. Ask for feedback if anything in this summary is unclear.

---
If you'd like, I can open a branch, commit this file, and push it now. Reply "yes" to proceed or request edits.
