import os
import json
from file_reader import read_file
from ai_service import send_to_ai
from validator import validate_json

INPUT_FOLDER = "input_files"
OUTPUT_FOLDER = "output"


def process_with_retry(text, max_retries=3):

    for attempt in range(max_retries):

        response = send_to_ai(text)
        is_valid, data = validate_json(response)

        if is_valid:
            return data

        print(f"Intento {attempt + 1} fallido... reintentando.")

    raise ValueError("La IA no devolvió JSON válido.")


def main():

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    for filename in os.listdir(INPUT_FOLDER):

        file_path = os.path.join(INPUT_FOLDER, filename)

        if not os.path.isfile(file_path):
            continue

        print(f"Procesando {filename}")

        text = read_file(file_path)

        try:
            data = process_with_retry(text)

            output_path = os.path.join(
                OUTPUT_FOLDER,
                f"{os.path.splitext(filename)[0]}.json"
            )

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            print(f"Guardado en {output_path}")

        except Exception as e:
            print(f"Error procesando {filename}: {e}")


if __name__ == "__main__":
    main()
