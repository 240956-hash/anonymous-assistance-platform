# Contribution process

Each team member commits and pushes their reviewed changes using their own
GitHub account and their own verified Git email. Do not change author details
to impersonate another contributor or backdate commits.

Branch from the current default branch. Include the actual YouTrack task ID in
the branch and pull request where confirmed. Use focused commits, explain
changed behaviour, and ask another team member to review before merging.

Run `python manage.py check`, `python manage.py makemigrations --check --dry-run`
and `python manage.py test`. Record any unrun checks accurately. Commit source
migrations, not a local SQLite database. Never commit `.env` or real requests.

Before stage submission, verify repository and YouTrack access for the
supervisor and committee. Once reviewed and approved, tag the selected commit
`prob-period-1`, as required by the submission instructions. Do not create the
submission tag on an unreviewed skeleton merely to satisfy a commit count.
