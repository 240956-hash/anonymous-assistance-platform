from django.test import SimpleTestCase

class PageTests(SimpleTestCase):
    def test_pages_render(self):
        for route in ("/", "/support/", "/request/", "/specialist/"):
            with self.subTest(route=route):
                response = self.client.get(route)
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, 'lang="en"')

    def test_specialist_view_is_explicitly_a_placeholder(self):
        self.assertContains(self.client.get("/specialist/"), "No real requests are shown.")

    def test_form_has_csrf_token_and_no_email_field(self):
        response = self.client.get("/request/")
        self.assertContains(response, "csrfmiddlewaretoken")
        self.assertNotContains(response, 'name="email"')
        self.assertContains(response, 'maxlength="5000"')

    def test_health_marker(self):
        self.assertEqual(self.client.get("/api/health/").json()["stage"], "skeleton")
