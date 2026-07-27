import json
from google import genai

from config import (
    GEMINI_API_KEY,
    GEMINI_MODEL
)


class GeminiProvider:

    def __init__(self):

        self.client = genai.Client(api_key=GEMINI_API_KEY)

    # ---------------------------------
    # Chat
    # ---------------------------------

    def generate(self, prompt):

        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        return response.text

    # ---------------------------------
    # Memory Extraction
    # ---------------------------------

    def extract_memory(self, message):

        prompt = f"""
        You are a memory extraction engine.

        Extract any long-term personal information about the user.

        Only extract information that is likely to remain true for weeks or months.

        Use concise snake_case keys.

        Examples of information to remember:

        - name
        - surname
        - nickname
        - age
        - birthday
        - city
        - country
        - email
        - phone
        - education
        - degree
        - college
        - university
        - job
        - company
        - designation
        - skills
        - favourite_color
        - favourite_food
        - favourite_movie
        - favourite_game
        - favourite_car
        - favourite_animal
        - favourite_language
        - hobbies
        - interests
        - programming_languages
        - dream_company
        - career_goal
        - pet_name
        - relationship_status (only if explicitly stated)

        Do NOT extract:

        - greetings
        - questions
        - temporary emotions
        - today's plans
        - jokes
        - examples
        - requests

        Correct obvious spelling mistakes.

        Return ONLY valid JSON.

        If nothing should be remembered, return:

        {{}}

        Message:

        {message}
        """

        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        text = response.text.strip()

        # Remove markdown if model accidentally returns it
        text = text.replace("```json", "").replace("```", "").strip()

        try:
            return json.loads(text)
        except Exception:
            print("Memory JSON Error:", text)
            return {}