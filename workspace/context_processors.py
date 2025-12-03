from django.utils import timezone


def current_date(_) -> dict:
    return {"current_date": timezone.now()}
