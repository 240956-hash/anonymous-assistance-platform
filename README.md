# Anonymous Assistance Platform

Initial diploma project skeleton for a proposed platform providing legal and
psychotherapeutic support to people affected by domestic violence.

This branch is an engineering prototype. It is not an operational support
service. Use fictional text only. There is no request storage endpoint,
specialist authentication flow, reply inbox, deletion job or emergency service.

## Local setup

Python 3.12 is recommended. Run in PowerShell from the repository root:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
$env:DJANGO_DEBUG = "1"
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ after the frontend commits are applied.
The health endpoint is http://127.0.0.1:8000/api/health/.
`.env.example` documents variables; it is not loaded automatically.
Without a configured secret in debug mode, a temporary development secret is
generated at startup; sessions will not persist across restarts.

For PostgreSQL, install `requirements-postgres.txt`, set `DB_ENGINE=postgresql`
and the `DB_*` variables, then run migrations. SQLite is only the local default;
PostgreSQL remains the proposed project database.

## Checks

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```

## Structure and ownership

- `config/`: Django configuration and URL routing — Aktoty.
- `core/`: data model, validation and API prototype — Aktoty.
- `templates/`, `static/`, `web/`: English interface prototype — Akerke.
- `tests/`, `.github/`, `docs/security/`: checks and security planning — Danial.

## Current behaviour

Valid request-shaped JSON is checked but receives HTTP 501 with `saved: false`.
No request record or access code is created. Invalid input receives HTTP 400.
The specialist page is a layout placeholder and contains no case data.
Health checks report process availability, not database readiness.

## Documentation

See `docs/architecture.md`, `docs/api.md`, `docs/frontend.md`,
`docs/security/threat-model.md` and `docs/testing.md` as their commits are added.
No survey responses, personal histories or participant details belong in this
repository. The survey's illustrative results are not empirical evidence.

Repository: https://github.com/240956-hash/anonymous-assistance-platform
YouTrack: https://240956.youtrack.cloud/projects/AAP

## Official technical references

- https://docs.djangoproject.com/en/5.2/intro/tutorial01/
- https://docs.djangoproject.com/en/5.2/topics/security/

Resolve the latest available Django 5.2 patch when installing. Record the
installed versions for reproducible evaluation of a particular project tag.
