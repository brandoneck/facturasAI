def process_with_retry(text, max_retries=3):

    for attempt in range(max_retries):

        response = send_to_ai(text)

        is_valid, data = validate_json(response)

        if is_valid:
            return data

        print(f"Intento {attempt + 1} fallido... reintentando.")

    raise ValueError("La IA no devolvió un JSON válido después de varios intentos.")
