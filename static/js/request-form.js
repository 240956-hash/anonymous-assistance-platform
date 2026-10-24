"use strict";
const form = document.getElementById("request-form");
if (form) {
  const button = document.getElementById("submit-button");
  const status = document.getElementById("request-status");
  const text = document.getElementById("request-text");
  const error = document.getElementById("text-error");
  button.disabled = false;
  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    error.textContent = "";
    status.textContent = "";
    text.removeAttribute("aria-invalid");
    if (!text.value.trim()) {
      error.textContent = "Enter a fictional question before continuing.";
      text.setAttribute("aria-invalid", "true");
      text.focus();
      return;
    }
    button.disabled = true;
    status.textContent = "Checking example input…";
    try {
      const response = await fetch(form.dataset.endpoint, {
        method: "POST", credentials: "same-origin", cache: "no-store",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": form.querySelector('[name="csrfmiddlewaretoken"]').value,
        },
        body: JSON.stringify({category: form.elements.category.value, text: text.value}),
      });
      const result = response.headers.get("content-type")?.includes("application/json")
        ? await response.json() : {};
      if (response.status === 501 && result.code === "prototype_only" && result.saved === false) {
        status.textContent = "Input checked. This prototype has not saved or sent your example.";
      } else if (response.status === 400) {
        status.textContent = "Input was rejected. Check the category and the 1–5,000 character limit. Nothing was saved.";
      } else {
        status.textContent = "The input could not be checked. This prototype does not store requests.";
      }
    } catch {
      status.textContent = "Connection failed. This prototype does not store requests.";
    } finally {
      button.disabled = false;
    }
  });
}
