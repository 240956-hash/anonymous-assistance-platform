# API prototype

`GET /api/health/` returns 200 and the service/stage marker. It does not inspect
the database or establish readiness for real cases.

`POST /api/requests/` accepts JSON with string fields `category` and `text`.
Categories: `legal`, `psychotherapeutic`. Trimmed text: 1–5000 characters.
Unexpected fields are rejected. Do not include names or contact details in
demonstration input. The form must obtain and send a Django CSRF token.

- 400: invalid JSON, fields, types or category/text validation.
- 403: missing/incorrect CSRF token when CSRF checks apply.
- 405: unsupported HTTP method.
- 413: request body exceeds the configured 32 KiB limit.
- 415: unsupported content type.
- 501: syntactically valid input; feature not implemented; `saved` is false.

Example fictional body:

```json
{"category": "legal", "text": "Fictional example for a validation test."}
```

There is no 201 response. No request UUID or access code is issued. No database
record is created. Response bodies never repeat the submitted description.
Infrastructure request logging and JSON error reporting still require review
before deployment; the prototype does not provide absolute anonymity.
