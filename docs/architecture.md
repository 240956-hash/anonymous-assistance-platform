# Initial architecture

Browser → Django templates / JSON API → validation and future access control
→ request processing → PostgreSQL (proposed target).

The skeleton uses SQLite for a local demonstration. The conceptual `Request`
entity is implemented as `AssistanceRequest` to avoid confusion with HTTP
requests. `Specialist` links to Django's user account. `Assignment` will relate
permitted specialists to requests. `Message` stores the author role, content
and timestamp. `AuditEvent` has only an operation, internal UUID and timestamp.

Models and migrations establish structure only. Model validators are not
automatically enforced by every direct ORM save, so future write services must
validate input explicitly and enforce access policy on every operation.

No name, phone, email or location field is required for an assistance request.
The access-secret field is reserved for a hash; secret generation, hashing,
verification and the reply inbox are not implemented in this skeleton.

`expires_at` is a schema field, not an implemented deletion mechanism. The
proposed retention periods in the diploma document still require approval.
Specialist verification and active flags default to false and do not by
themselves provide an authorisation policy.

Next steps: approve the API contract and threat model; implement write/read
services and assignment-based access; implement retention jobs; verify each
path using synthetic data before considering any real use.
