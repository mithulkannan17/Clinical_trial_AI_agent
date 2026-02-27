import re
import random


PROMPT_DESCRIPTION = """
Clinical Trial AI Agent

Agent extracts structured clinical trial data
from unstructured medical text.

Implements:

- AI-style extraction
- Retry logic
- Structured schema
"""


def extract_success_rate(text):

    match = re.search(r'(\d+)\s*%', text)

    if match:
        return float(match.group(1))

    return None


def extract_phase(text):

    match = re.search(r'Phase\s*\d', text, re.IGNORECASE)

    if match:
        return match.group(0)

    return None


def extract_company(text):

    companies = [

        "Pfizer",
        "Moderna",
        "AstraZeneca",
        "Bharat Biotech",
        "Serum Institute"

    ]

    for c in companies:

        if c.lower() in text.lower():

            return c

    return None



def extract_duration(text):

    match = re.search(r'(\d+)\s*year', text)

    if match:

        return match.group(0)

    return None



def extract_disease(text):

    words = text.split()

    if "against" in words:

        idx = words.index("against")

        return words[idx + 1] + " virus"

    return "Unknown"



def classify_risk(success_rate):

    if success_rate is None:
        return "Unknown"

    if success_rate < 50:
        return "High Risk"

    if success_rate < 80:
        return "Moderate"

    return "Curable"



def confidence_score(data):

    filled = 0

    total = len(data)

    for v in data.values():

        if v is not None:

            filled += 1

    return round(filled / total, 2)



def run_agent(text):

    for attempt in range(3):

        try:

            data = {}

            data["disease"] = extract_disease(text)

            data["trial_phase"] = extract_phase(text)

            data["success_rate"] = extract_success_rate(text)

            data["company"] = extract_company(text)

            data["vaccine_name"] = data["company"]

            data["duration"] = extract_duration(text)

            data["risk_level"] = classify_risk(
                data["success_rate"]
            )

            data["confidence"] = confidence_score(data)


            return data

        except Exception:

            continue


    raise Exception("Agent failed after retries")