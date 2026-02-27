from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def explain_disease(disease):

    prompt = f"""
Explain the disease {disease} in simple medical terms.

Rules:
- Maximum 5 lines
- Simple language
- No treatment advice
- Only explanation
"""

    try:

        response = client.chat.completions.create(

            # Updated working model
            model="llama-3.1-8b-instant",

            messages=[
                {"role": "user", "content": prompt}
            ]

        )

        return response.choices[0].message.content

    except Exception as e:

        return "AI explanation unavailable: " + str(e)