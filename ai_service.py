import os
from dotenv import load_dotenv
from google import genai
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("No se encontró GEMINI_API_KEY en el .env")

client = genai.Client(api_key=api_key)


# print("API KEY:", api_key)

def send_to_ai(text):

    prompt = f"""
    Extrae del siguiente texto:

    - nombre
    - monto
    - fecha
    - tipo_solicitud (Venta, Queja o Factura)

    Devuelve ÚNICAMENTE un JSON válido, sin texto adicional ni explicaciones, ni formato extra.
    Formato obligatorio:
    {{
        "nombre": "string",
        "monto": "float | null",
        "fecha": "YYYY-MM-DD | null",
        "tipo_solicitud": "Venta | Queja | Factura"
    }}

    Texto:
    {text}
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text