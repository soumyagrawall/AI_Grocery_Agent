# agent.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")


def parse_grocery_note(note):
    prompt = f"""
You are a smart AI grocery assistant.

Your job is to extract all grocery items from any kind of user note. The note may be messy, informal, shorthand, or unstructured.

For each item, extract:
- item name
- quantity (e.g., 1kg, 2 bottles, etc.)
- brand name (if mentioned)

If brand or quantity is not mentioned, write "None".

Respond ONLY in valid JSON list format like this:
[
  {{"item": "item name", "quantity": "amount", "brand": "brand name"}},
  ...
]

Grocery Note:
\"\"\"
{note}
\"\"\"
"""

    response = model.generate_content(prompt)
    return response.text


# Test it
if __name__ == "__main__":
    sample_note = """
    2 packs Amul cheese, 1kg rice, 5 bananas, 2 litres Nestle milk, 1 dozen eggs, lays chips
    """

    result = parse_grocery_note(sample_note)
    print("🛒 Extracted Grocery List:")
    print(result)
