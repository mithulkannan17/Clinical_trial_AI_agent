import re


# block diagnosis advice

BLOCKED_PHRASES = [
    "you should take",
    "recommended treatment",
    "patient should",
    "take this medicine"
]


def check_blocked_phrases(text: str):

    text = text.lower()

    for phrase in BLOCKED_PHRASES:
        if phrase in text:
            return False

    return True



# fake medication check

APPROVED_MEDICATIONS = [

    "pfizer",
    "moderna",
    "astrazeneca",
    "bharat biotech",
    "serum institute",


    "university",
    "institute",
    "hospital",
    "national",
    "health",
    "research",
    "biotech",
    "pharma",
    "inc",
    "ltd"

]


def medication_allowed(name: str):

    if name is None:
        return True

    name = name.lower()

    for med in APPROVED_MEDICATIONS:
        if med in name:
            return True

    return False