import json
import google.generativeai as genai


def configure_gemini(api_key):

    genai.configure(
        api_key=api_key
    )

    return genai.GenerativeModel(
        "gemini-2.5-flash"
    )


def rank_candidate(model, prompt):

    response = model.generate_content(
        prompt
    )

    text = response.text.strip()

    # Remove markdown if Gemini wraps JSON
    if text.startswith("```json"):
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

    try:
        return json.loads(text)

    except Exception:

        print("\nGemini returned:\n")
        print(text)

        raise