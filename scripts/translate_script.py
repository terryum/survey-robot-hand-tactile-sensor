#!/usr/bin/env python3
"""Translate slide scripts to Korean using Gemini API."""

import os
import sys
from google import genai


def translate_to_korean(input_path: str, output_path: str):
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    client = genai.Client(api_key=api_key)

    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into chunks to handle large content — main presentation + Q&A
    # Find the Q&A section split point
    qa_split = content.find("# Q&A Session")
    if qa_split > 0:
        main_part = content[:qa_split]
        qa_part = content[qa_split:]
    else:
        main_part = content
        qa_part = ""

    translated_parts = []
    for i, part in enumerate([main_part, qa_part]):
        if not part.strip():
            continue
        label = "Main Presentation" if i == 0 else "Q&A Session"
        print(f"Translating {label}...")

        prompt = f"""Translate the following presentation script from English to Korean.

Rules:
- Keep all markdown formatting (headers, horizontal rules, slide markers like "--- Slide X: ... ---")
- Translate the slide marker titles to Korean as well
- Translate naturally and fluently — this is a spoken presentation, so use conversational Korean (구어체)
- Keep proper nouns (CoinFT, UMI-FT, Stanford, Sunday Robotics, etc.) in English
- Keep technical terms in their commonly used form (e.g., force torque → 힘/토크, tactile sensing → 촉각 센싱)
- Do NOT add or remove any content
- The header "# Presentation Script" should become "# 발표 스크립트"
- "# Main Presentation" → "# 본발표"
- "# Q&A Session" → "# Q&A 세션"

Text to translate:
{part}"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[prompt],
            config=genai.types.GenerateContentConfig(
                max_output_tokens=65536,
            ),
        )
        translated_parts.append(response.text)
        print(f"  Done ({len(response.text)} chars)")

    result = "\n".join(translated_parts)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"Korean translation saved to {output_path}")


if __name__ == "__main__":
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base, "data-source", "seminar-hojung-choi")

    translate_to_korean(
        input_path=os.path.join(data_dir, "slide_scripts.md"),
        output_path=os.path.join(data_dir, "slide_scripts_ko.md"),
    )
