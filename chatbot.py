from google.genai.errors import ClientError

from config import SYSTEM_PROMPT
from memory import MemoryManager
from conversation import ConversationManager
from nlp_utils import preprocess
from model_router import ModelRouter


class AIChatbot:

    def __init__(self):

        # AI Model Router
        self.router = ModelRouter()

        # Memory Manager
        self.memory = MemoryManager()

        # Conversation Manager
        self.conversation = ConversationManager()

    # ---------------------------------------------------------
    # Memory Detection
    # ---------------------------------------------------------


    # ---------------------------------------------------------
    # Build Prompt
    # ---------------------------------------------------------

    def build_prompt(self, user_message, selected_model):

        memory = self.memory.recall()

        if memory:

            memory_text = ""

            for key, value in memory.items():

                memory_text += f"• {key.title()}: {value}\n"

        else:

            memory_text = "No user information stored."

        history = self.conversation.format_for_prompt()

        processed = preprocess(user_message)

        prompt = f"""
{SYSTEM_PROMPT}

====================================================
CURRENT MODEL
====================================================

Current AI Provider:

{selected_model}

Rules:

- You MUST identify yourself as {selected_model}.
- Never say you are Gemini unless Current Model is Gemini.
- Never say you are Groq unless Current Model is Groq.
- Never say you are Mistral unless Current Model is Mistral.
- If the user asks which model you use,
answer using the Current Model section above.
- Never invent another model.

====================================================
USER PROFILE
====================================================

{memory_text}

====================================================
PREVIOUS CONVERSATION
====================================================

{history}

====================================================
CURRENT USER MESSAGE
====================================================

{user_message}

====================================================
NLP ANALYSIS
====================================================

{processed}

====================================================
IMPORTANT
====================================================

1. USER PROFILE belongs ONLY to the user.

2. Never confuse yourself with the user.

3. If user asks:
"What is my name?"

Use USER PROFILE.

4. If user asks:
"What is your name?"

Reply with your assistant name.

5. If user asks remembered facts,
use USER PROFILE.

6. If information isn't available,
say you don't know.

7. Be natural.

8. Avoid repetitive wording.

9. Keep answers concise unless asked for detail.

10. Never claim another AI provider.
"""

        return prompt

    # ---------------------------------------------------------
    # Chat
    # ---------------------------------------------------------

    def chat(self, user_message, selected_model="Gemini"):

        # -----------------------------------------------------
        # Memory Extraction (Dynamic)
        # -----------------------------------------------------

        try:

            print("\n========== MEMORY EXTRACTION ==========")
            print("User Message:", user_message)

            new_memory = self.router.extract_memory(
                user_message,
                selected_model
            )

            print("Extracted Memory:", new_memory)

            if isinstance(new_memory, dict) and new_memory:

                current_memory = self.memory.recall()

                aliases = {
                    "location": "city",
                    "current_location": "city",
                    "colour": "favourite_color",
                    "favorite_color": "favourite_color",
                    "favorite_colour": "favourite_color",
                    "mail": "email",
                    "full_name": "name"
                }

                normalized = {}

                for key, value in new_memory.items():
                    key = aliases.get(key.lower(), key.lower())
                    normalized[key] = value

                current_memory.update(normalized)

                self.memory.update_memory(current_memory)

                print("Current Memory:")
                print(self.memory.recall())

            else:
                print("Nothing extracted.")

            print("=======================================\n")

        except Exception as e:
            print("Memory Extraction Error:", e)

        # -------------------------------
        # Save User Message
        # -------------------------------

        self.conversation.add_user_message(user_message)

        # -------------------------------
        # Handle Provider Questions Yourself
        # -------------------------------

        msg = user_message.lower()

        model_queries = [

            "which model",
            "what model",
            "which ai",
            "what ai",
            "what llm",
            "which llm",
            "which provider",
            "who powers you",
            "what powers you",
            "which model are you using",
            "what model are you using",
            "are you gemini",
            "are you groq",
            "are you mistral"
        ]

        if any(q in msg for q in model_queries):

            provider_reply = {

                "Gemini":
                    "I'm currently powered by **Google Gemini 2.5 Flash**.",

                "Groq":
                    "I'm currently using **Groq**. The underlying model depends on the model configured in your Groq provider.",

                "Mistral":
                    "I'm currently powered by **Mistral AI**.",

            }

            answer = provider_reply.get(
                selected_model,
                f"I'm currently using **{selected_model}**."
            )

            self.conversation.add_bot_message(answer)

            return answer

        # -------------------------------
        # Build Prompt
        # -------------------------------

        prompt = self.build_prompt(
            user_message,
            selected_model
        )

        # -------------------------------
        # Generate Response
        # -------------------------------

        try:

            answer = self.router.generate(
                prompt,
                selected_model
            )

        except ClientError as e:

            if "429" in str(e):

                answer = (
                    "⚠️ Gemini quota exceeded.\n\n"
                    "Please switch to Groq or Mistral, or try again later."
                )

            else:

                answer = f"API Error:\n\n{e}"

        except Exception as e:

            answer = f"Unexpected Error:\n\n{e}"

        # -------------------------------
        # Save Response
        # -------------------------------

        self.conversation.add_bot_message(answer)

        return answer

    # ---------------------------------------------------------
    # Utilities
    # ---------------------------------------------------------

    def clear_chat(self):

        self.conversation.clear()

    def clear_memory(self):

        self.memory.clear()

    def show_memory(self):

        return self.memory.recall()

    def show_history(self):

        return self.conversation.get_history()

