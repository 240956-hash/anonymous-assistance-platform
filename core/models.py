import uuid
from django.conf import settings
from django.core.validators import MaxLengthValidator
from django.db import models

class AssistanceRequest(models.Model):
    class Category(models.TextChoices):
        LEGAL = "legal", "Legal assistance"
        PSYCHOTHERAPEUTIC = "psychotherapeutic", "Psychotherapeutic assistance"

    class Status(models.TextChoices):
        NEW = "new", "New"
        IN_PROGRESS = "in_progress", "In progress"
        ANSWERED = "answered", "Reply provided"
        CLOSED = "closed", "Closed"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=24, choices=Category.choices)
    text = models.TextField(validators=[MaxLengthValidator(5000)])
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    access_secret_hash = models.CharField(max_length=255)

    def __str__(self):
        return f"Request {self.pk}"

class Specialist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=24, choices=AssistanceRequest.Category.choices)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

class Assignment(models.Model):
    request = models.ForeignKey(AssistanceRequest, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["request", "specialist"], name="unique_request_specialist"
        )]

class Message(models.Model):
    class AuthorRole(models.TextChoices):
        USER = "user", "User"
        SPECIALIST = "specialist", "Specialist"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    request = models.ForeignKey(AssistanceRequest, on_delete=models.CASCADE)
    author_role = models.CharField(max_length=16, choices=AuthorRole.choices)
    text = models.TextField(validators=[MaxLengthValidator(5000)])
    created_at = models.DateTimeField(auto_now_add=True)

class AuditEvent(models.Model):
    # Do not add request content, access secrets, names or contact details here.
    created_at = models.DateTimeField(auto_now_add=True)
    operation = models.CharField(max_length=40)
    subject_id = models.UUIDField()
