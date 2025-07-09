from dotenv import load_dotenv
import os
import google.generativeai as genai


class GeminiClient:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("models/gemini-2.5-flash")

    def generate_prompt_response(self, prompt: str):
        response = self.model.generate_content(prompt)
        return response.text
