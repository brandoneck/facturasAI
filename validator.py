import json


def validate_json(response_text):

    try:
        data = json.loads(response_text)
    except json.JSONDecodeError:
        return False, None

    required_keys = ["nombre", "monto", "fecha", "tipo_solicitud"]

    for key in required_keys:
        if key not in data:
            return False, None

    return True, data