def grade_response(task_type, response):
    response = response.lower()

    if task_type == "easy":
        if "track" in response or "order" in response:
            return 0.75
        else:
            return 0.25

    elif task_type == "medium":
        if "refund" in response or "replacement" in response:
            return 0.8
        else:
            return 0.35

    elif task_type == "hard":
        if "refund" in response or "escalate" in response:
            return 0.85
        else:
            return 0.4

    return 0.5
