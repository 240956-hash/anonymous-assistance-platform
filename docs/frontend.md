# Frontend prototype

Routes: `/`, `/support/`, `/request/`, `/specialist/`.
Django templates and plain CSS/JavaScript avoid a separate build tool in the
initial skeleton. This is a prototyping choice, not a final frontend decision.

Labels, keyboard focus, a skip link, responsive layout and a live status region
support basic access. The form uses the category values in the API contract.
It sends a CSRF token and displays the 501 response as an unimplemented feature,
never as a successful request. No content is put in URLs, browser storage or
console logs by this frontend.

The specialist layout is publicly viewable because it contains only explanatory
text. It is not an authenticated dashboard and exposes no case data.

Manual review: keyboard-only navigation; 320/768/1280 px viewports; zoom at
200%; empty and whitespace-only text; exactly 5,000 characters; invalid
category via API; network failure; JavaScript disabled; status announcement
with a screen reader. Record browser/version and observed results after running
these checks. No accessibility certification or user study is claimed.

Further work: agree help text with support professionals; validate the flow
using fictional tasks; implement secure reply access; localise approved text.
