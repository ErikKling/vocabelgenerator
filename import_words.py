import json
import re
from gemini_api import GeminiClient

ENGLISH = "google-10000-english-no-swears.txt"

def load_words_from_file(filepath, limit=5):
    with open(filepath, "r") as f:
        return [line.strip() for line in f.readlines()[:limit]]

def clean_json_string(text):
    """Entfernt ```json und ``` aus der Gemini-Antwort"""
    return re.sub(r"```json|```", "", text).strip()

def generate_prompt(word: str) -> str:
    return f"""
Gib für das englische Wort "{word}":
– das Wort selbst
– die deutsche Übersetzung
– einen einfachen englischen Beispielsatz mit dem Wort

Bitte antworte exakt im folgenden JSON-Format ohne zusätzliche Erklärungen:

{{
  "word": "...",
  "translation": "...",
  "example": "..."
}}
"""

def main():
    words = load_words_from_file(ENGLISH, limit=5)
    client = GeminiClient()

    for word in words:
        prompt = generate_prompt(word)
        response = client.generate_prompt_response(prompt)

        cleaned = clean_json_string(response)

        try:
            data = json.loads(cleaned)
            print(f"✅ {word}: {data}")
        except json.JSONDecodeError:
            print(f"⚠️ Fehler bei Wort '{word}':\n{response}\n")

if __name__ == "__main__":
    main()