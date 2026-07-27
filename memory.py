import json
import os

MEMORY_FILE = "memory.json"


class MemoryManager:

    def __init__(self):

        if not os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "w") as file:
                json.dump({}, file, indent=4)

    def load(self):

        try:

            with open(MEMORY_FILE, "r") as file:
                return json.load(file)

        except (json.JSONDecodeError, FileNotFoundError):

            return {}

    def save(self, memory):

        with open(MEMORY_FILE, "w") as file:

            json.dump(memory, file, indent=4)

    def remember(self, key, value):

        memory = self.load()

        memory[key] = value

        self.save(memory)

    def recall(self):

        return self.load()

    def forget(self, key):

        memory = self.load()

        if key in memory:

            del memory[key]

            self.save(memory)

    def clear(self):

        self.save({})

    def exists(self, key):

        memory = self.load()

        return key in memory

    def update_memory(self, new_data):

        memory = self.load()

        for key, value in new_data.items():

            if value not in ["", None]:
                memory[key] = value

        self.save(memory)