from providers.gemini_provider import GeminiProvider
from providers.groq_provider import GroqProvider
from providers.mistral_provider import MistralProvider


class ModelRouter:

    def __init__(self):

        self.providers = {

            "Gemini": GeminiProvider(),

            "Groq": GroqProvider(),

            "Mistral": MistralProvider()

        }

    # ----------------------------

    def generate(self, prompt, model_name):

        provider = self.providers.get(model_name)

        if provider is None:
            raise Exception(f"Unknown model: {model_name}")

        return provider.generate(prompt)

    # ----------------------------

    def extract_memory(self, message, model_name):

        provider = self.providers.get(model_name)

        if provider is None:
            return {}

        return provider.extract_memory(message)