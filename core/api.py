import json
from django.core.exceptions import RequestDataTooBig
from django.http import JsonResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.http import require_POST
from .forms import AssistanceRequestForm

@never_cache
@sensitive_post_parameters()
@require_POST
def request_prototype(request):
    if request.content_type != "application/json":
        return JsonResponse({"error": "Use application/json.", "saved": False}, status=415)
    try:
        payload = json.loads(request.body)
    except RequestDataTooBig:
        return JsonResponse({"error": "Payload is too large.", "saved": False}, status=413)
    except (ValueError, UnicodeDecodeError):
        return JsonResponse({"error": "Invalid JSON.", "saved": False}, status=400)
    if not isinstance(payload, dict) or set(payload) - {"category", "text"}:
        return JsonResponse({"error": "Only category and text are accepted.", "saved": False}, status=400)
    if any(not isinstance(payload.get(key), str) for key in ("category", "text")):
        return JsonResponse({"error": "Category and text must be strings.", "saved": False}, status=400)
    form = AssistanceRequestForm(payload)
    if not form.is_valid():
        return JsonResponse({"errors": form.errors.get_json_data(), "saved": False}, status=400)
    # Deliberately no ORM write, content echo, secret generation or logging.
    return JsonResponse({
        "code": "prototype_only", "saved": False,
        "message": "Input checked. Submission and storage are not implemented.",
    }, status=501)
