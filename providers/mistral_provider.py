import json
import requests

from config import (
    MISTRAL_API_KEY,
    MISTRAL_MODEL
)


class MistralProvider:

    def generate(self, prompt):

        response = requests.post(

            "https://api.mistral.ai/v1/chat/completions",

            headers={
                "Authorization": f"Bearer {MISTRAL_API_KEY}",
                "Content-Type": "application/json"
            },

            json={
                "model": MISTRAL_MODEL,

                "messages":[
                    {
                        "role":"user",
                        "content":prompt
                    }
                ]
            }

        )

        data = response.json()

        return data["choices"][0]["message"]["content"]

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

        response = requests.post(

            "https://api.mistral.ai/v1/chat/completions",

            headers={
                "Authorization": f"Bearer {MISTRAL_API_KEY}",
                "Content-Type": "application/json"
            },

            json={

                "model": MISTRAL_MODEL,

                "temperature": 0,

                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }

        )

        data = response.json()

        text = data["choices"][0]["message"]["content"].strip()

        text = text.replace("```json", "").replace("```", "").strip()

        try:
            return json.loads(text)

        except Exception:

            print("Mistral Memory Parse Error:")
            print(text)

            return {}