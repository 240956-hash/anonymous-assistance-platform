# Local verification record

Date: 23 October 2026. Environment: Windows, Python 3.12.14, Django 5.2.18,
SQLite in-memory test database. Only fictional fixtures were used.

- `python manage.py check`: passed, no issues.
- `python manage.py makemigrations --check --dry-run`: passed, no changes.
- `python manage.py test --verbosity 2`: 14 tests discovered and passed.
- JavaScript parser check with `node --check static/js/request-form.js`: passed.

The complete assembled skeleton was tested, not the remote repository. GitHub
Actions, PostgreSQL, manual browser/screen-reader checks, load testing and a
production security assessment have not been run. No Git commit or remote tag
has been created as part of preparing these packages.

`requirements-tested.txt` contains the resolved dependency versions used for
local checks. Reproduce them with:

```text
python -m pip install -r requirements.txt -c requirements-tested.txt
```

Add the actual commit ID and re-run the checks after applying the packages.
