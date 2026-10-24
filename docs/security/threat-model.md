# Initial threat model

## Assets and boundaries

Proposed assets: request text, replies, the access secret, specialist sessions,
assignments and deletion schedules. Browser → HTTPS/API → application → database
and hosting/logging infrastructure are separate trust boundaries. A user's
device is outside the platform's trusted boundary.

## Threats and planned controls

- Guessing or disclosing a request identifier: require a high-entropy secret,
  store only its hash, and check access on every operation. Not implemented.
- Another specialist reading a case: assignment-based server-side checks and
  negative tests. Models exist; the access service is not implemented.
- Leaking content through logs, URLs or notifications: never put content or
  secrets in URLs, avoid content logging, and keep external notifications off
  until explicitly agreed. Hosting and exception reporting require review.
- Injection and cross-site requests: validate types and lengths, keep Django
  autoescaping and CSRF middleware, use the ORM, and reject extra fields.
- Repeated submissions or abuse: rate limits, idempotency and monitoring rules
  are planned. No production abuse protection is implemented.
- Over-retention: agree expiry and backup retention; implement deletion and
  test it. An expiry field alone does not remove data.

## Limits

A monitored device, compromised browser or hosting provider may expose data.
Not collecting a real name does not guarantee anonymity. This skeleton has no
anonymity audit, penetration-test result, clinical evidence or production
readiness claim. The JSON endpoint validates fictional input and does not save it.

## Verification priorities

Verify CSRF, rejected inputs, content not echoed, no writes on the prototype
path, and absence of case data in the placeholder view. Later add a complete
user/specialist/other-specialist permission matrix before enabling persistence.
