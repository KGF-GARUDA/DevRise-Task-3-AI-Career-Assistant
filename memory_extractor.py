import re


def extract_memory(message):

    memory = {}

    msg = message.strip()

    # -------------------------
    # Name
    # -------------------------

    patterns = [
        r"my name is (.+)",
        r"i am (.+)",
        r"i'm (.+)",
        r"call me (.+)"
    ]

    for pattern in patterns:

        match = re.search(pattern, msg, re.IGNORECASE)

        if match:

            memory["name"] = match.group(1).strip().title()
            break

    # -------------------------
    # Email
    # -------------------------

    match = re.search(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        msg
    )

    if match:

        memory["email"] = match.group()

    # -------------------------
    # City
    # -------------------------

    match = re.search(
        r"(?:i live in|i am from|my city is)\s+(.+)",
        msg,
        re.IGNORECASE
    )

    if match:

        memory["city"] = match.group(1).strip().title()

    # -------------------------
    # College
    # -------------------------

    match = re.search(
        r"(?:i study at|i study in|i studied at|college is)\s+(.+)",
        msg,
        re.IGNORECASE
    )

    if match:

        memory["college"] = match.group(1).strip()

    # -------------------------
    # Education
    # -------------------------

    match = re.search(
        r"(?:i am studying|i study|i completed|i have completed)\s+(.+)",
        msg,
        re.IGNORECASE
    )

    if match:

        memory["education"] = match.group(1).strip()

    # -------------------------
    # Favourite Language
    # -------------------------

    match = re.search(
        r"(?:favorite|favourite)\s+(?:programming\s+)?language\s+is\s+(.+)",
        msg,
        re.IGNORECASE
    )

    if match:

        memory["favorite_language"] = match.group(1).strip().title()

    # -------------------------
    # Favourite Color
    # -------------------------

    match = re.search(
        r"(?:favorite|favourite)\s+color\s+is\s+(.+)",
        msg,
        re.IGNORECASE
    )

    if match:

        memory["favorite_color"] = match.group(1).strip().title()

    # -------------------------
    # Favourite Animal
    # -------------------------

    match = re.search(
        r"(?:favorite|favourite)\s+animal\s+is\s+(.+)",
        msg,
        re.IGNORECASE
    )

    if match:

        memory["favorite_animal"] = match.group(1).strip().title()

    # -------------------------
    # Hobby
    # -------------------------

    match = re.search(
        r"(?:my hobby is|my hobbies are|i like)\s+(.+)",
        msg,
        re.IGNORECASE
    )

    if match:

        memory["hobby"] = match.group(1).strip()

    # -------------------------
    # Goal
    # -------------------------

    match = re.search(
        r"(?:my goal is|my dream is|i want to become)\s+(.+)",
        msg,
        re.IGNORECASE
    )

    if match:

        memory["goal"] = match.group(1).strip()

    return memory