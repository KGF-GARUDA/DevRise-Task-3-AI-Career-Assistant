class ConversationManager:

    def __init__(self, max_history=20):
        """
        Stores the current conversation.
        max_history = maximum number of messages to keep
        """
        self.max_history = max_history
        self.history = []

    def add_user_message(self, message):
        """Add a user message to history."""
        self.history.append({
            "role": "user",
            "text": message
        })
        self._trim_history()

    def add_bot_message(self, message):
        """Add a bot response to history."""
        self.history.append({
            "role": "assistant",
            "text": message
        })
        self._trim_history()

    def get_history(self):
        """Return the conversation history."""
        return self.history

    def clear(self):
        """Clear the current conversation."""
        self.history = []

    def format_for_prompt(self):
        """
        Convert conversation history into text
        that can be inserted into the Gemini prompt.
        """
        if not self.history:
            return "No previous conversation."

        formatted = ""

        for msg in self.history:
            role = "User" if msg["role"] == "user" else "Assistant"
            formatted += f"{role}: {msg['text']}\n"

        return formatted

    def _trim_history(self):
        """
        Keep only the latest messages.
        """
        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history:]