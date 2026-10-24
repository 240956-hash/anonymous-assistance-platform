import json
from django.test import Client, TestCase
from core.models import AssistanceRequest

class RequestPrototypeTests(TestCase):
    def send(self, payload):
        return self.client.post("/api/requests/", data=json.dumps(payload), content_type="application/json")

    def test_valid_input_is_not_saved_or_echoed(self):
        text = "Fictional example that must not be echoed."
        response = self.send({"category": "legal", "text": text})
        self.assertEqual(response.status_code, 501)
        self.assertFalse(response.json()["saved"])
        self.assertNotIn(text, response.content.decode())
        self.assertEqual(AssistanceRequest.objects.count(), 0)
        self.assertIn("no-store", response.headers["Cache-Control"])

    def test_invalid_inputs_never_create_records(self):
        payloads = [
            {}, [], {"category": "unknown", "text": "Example"},
            {"category": "legal", "text": "   "},
            {"category": "legal", "text": "x" * 5001},
            {"category": "legal", "text": 123},
            {"category": "legal", "text": "Example", "email": "fictional@example.invalid"},
        ]
        for payload in payloads:
            with self.subTest(payload_type=type(payload).__name__):
                self.assertEqual(self.send(payload).status_code, 400)
        self.assertEqual(AssistanceRequest.objects.count(), 0)

    def test_length_boundary_and_second_category(self):
        self.assertEqual(self.send({"category": "psychotherapeutic", "text": "x" * 5000}).status_code, 501)

    def test_invalid_json(self):
        response = self.client.post("/api/requests/", data="{", content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_content_type_and_method(self):
        self.assertEqual(self.client.post("/api/requests/", data="example", content_type="text/plain").status_code, 415)
        self.assertEqual(self.client.get("/api/requests/").status_code, 405)

    def test_payload_limit(self):
        self.assertEqual(self.send({"category": "legal", "text": "x" * 40000}).status_code, 413)

    def test_csrf_enforced(self):
        client = Client(enforce_csrf_checks=True)
        payload = json.dumps({"category": "legal", "text": "Fictional example"})
        denied = client.post("/api/requests/", data=payload, content_type="application/json")
        self.assertEqual(denied.status_code, 403)
        client.get("/request/")
        token = client.cookies["csrftoken"].value
        accepted = client.post("/api/requests/", data=payload, content_type="application/json", HTTP_X_CSRFTOKEN=token)
        self.assertEqual(accepted.status_code, 501)
