# Verification scope

Run from the repository root after installing dependencies and setting
`DJANGO_DEBUG=1` for local testing:

```text
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test --verbosity 2
```

Automated coverage includes the health marker, page rendering, CSRF rejection
and acceptance, invalid JSON/types/lengths/fields, the 5,000-character boundary,
payload limit, method/content-type restrictions, no persistence or content
echo on the prototype path, specialist defaults and unique assignments.

These tests do not establish a working authorisation scheme, secure deletion,
protection on monitored devices, PostgreSQL behaviour, load performance,
accessibility compliance or clinical effectiveness. Those are separate tasks.
The test database contains fictional fixtures only and is created/destroyed by
Django. No real survey responses or user requests are used.

For each actual evaluation, record date, commit, Python/Django versions,
operating system, database, commands and observed results. GitHub Actions must
be observed on the pushed commit before claiming remote CI passed. A workflow
file alone is not a successful CI run. See `docs/frontend.md` for manual checks.
