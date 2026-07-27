import json
from groq import Groq

from config import (
    GROQ_API_KEY,
    GROQ_MODEL
)


class GroqProvider:

    def __init__(self):

        self.client = Groq(api_key=GROQ_API_KEY)

    # ---------------------------------
    # Chat
    # ---------------------------------

    def generate(self, prompt):

        response = self.client.chat.completions.create(

            model=GROQ_MODEL,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

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

        response = self.client.chat.completions.create(

            model=GROQ_MODEL,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0
        )

        text = response.choices[0].message.content.strip()

        # Remove markdown if model returns ```json
        text = text.replace("```json", "").replace("```", "").strip()

        try:
            return json.loads(text)

        except Exception:
            print("Groq Memory Parse Error:")
            print(text)
            return {}