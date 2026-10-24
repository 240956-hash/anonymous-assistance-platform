from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from django.test import TestCase
from core.models import AssistanceRequest, Assignment, Specialist

class SchemaTests(TestCase):
    def test_specialist_is_not_active_or_verified_by_default(self):
        user = get_user_model().objects.create_user(username="fictional-specialist")
        specialist = Specialist.objects.create(user=user, role="legal")
        self.assertFalse(specialist.is_active)
        self.assertFalse(specialist.is_verified)

    def test_duplicate_assignment_is_rejected(self):
        request = AssistanceRequest.objects.create(category="legal", text="Fictional fixture", access_secret_hash="fixture-only-not-a-real-hash")
        user = get_user_model().objects.create_user(username="fictional-specialist")
        specialist = Specialist.objects.create(user=user, role="legal")
        Assignment.objects.create(request=request, specialist=specialist)
        with self.assertRaises(IntegrityError), transaction.atomic():
            Assignment.objects.create(request=request, specialist=specialist)

    def test_request_label_does_not_expose_text(self):
        request = AssistanceRequest(category="legal", text="Fictional confidential phrase")
        self.assertNotIn(request.text, str(request))
