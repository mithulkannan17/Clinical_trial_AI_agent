**Clinical Trial Intelligence AI Agent System**

*Orchestrating Data, Validation, and Insight for Medical Research*

Medical research is currently buried under what I call the "Fog of Unstructured Information". Right now, vital trial data is scattered across thousands of PDFs, registries, and dense research papers. I built this system to act as an intelligent orchestration layer that doesn't just "read" this data, but actually validates and structures it into something usable for researchers in real-time.
The goal was to replace the hours spent manually hunting through abstracts with a centralized, "safe" source of truth

**How It Works (The Architecture)**
Instead of relying on a single prompt, I designed a modular backend using FastAPI where each agent has a specialized role:
* The Tool Agent: The "structured thinker" that maps messy medical text into strict, standardized JSON schemas.
* The Scraper Agent: LLMs have knowledge cutoffs, so I used BeautifulSoup to fetch live updates directly from the web.
* The Explanation Agent: Uses Gemini/Groq to translate complex medical jargon into clear, patient-friendly narratives.
* The Safety Layer: A proactive gatekeeper using Pydantic to enforce data integrity and custom Guardrails to block unsafe outputs.

**Challenges Faced & Solutions**

**1. The "Hallucination" Problem**
The Challenge: In early testing, the LLM would occasionally "invent" success rates or confuse phase 2 trials with phase 3 because the source text was too dense.
The Solution: I implemented Pydantic Validation. By forcing the AI to output data into a strict schema, the system now performs "Completeness Checks". If a required field (like trial_phase) is missing or formatted incorrectly, the safety layer catches it before it ever reaches the user.

**2. Handling Real-Time Accuracy**
The Challenge: Static datasets are useless for fast-moving research. I needed a way to ensure the intelligence was current with the latest disease identifications.
The Solution: I integrated a Live Scraper Agent using Python Requests. Instead of just "knowing" things, the system goes out to the web to fetch live data beyond static datasets.

**Tech Stack**
* Core AI: Python, Gemini & Groq LLMs
* Backend: FastAPI 
* Data Validation: Pydantic
* Web Scraping: BeautifulSoup & Requests
* UI/UX: Inter & JetBrains Mono


