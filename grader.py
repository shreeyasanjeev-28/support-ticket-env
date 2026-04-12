def grade_easy(response):
    response = response.lower()
    return 0.8 if "order" in response or "track" in response else 0.2


def grade_medium(response):
    response = response.lower()
    return 0.85 if "refund" in response or "replacement" in response else 0.3


def grade_hard(response):
    response = response.lower()
    return 0.9 if "refund" in response or "escalate" in response else 0.4
