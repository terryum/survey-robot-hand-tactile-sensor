#!/usr/bin/env python3
"""Match transcript text to PDF slides using Gemini LLM."""

import os
import sys
import json
from google import genai

def load_pdf_content(json_path: str) -> str:
    """Load PDF page content and format for LLM."""
    with open(json_path, "r", encoding="utf-8") as f:
        pages = json.load(f)

    lines = []
    for p in pages:
        text = p["text"].strip() if p["text"].strip() else "(image-only slide, no text)"
        lines.append(f"=== SLIDE {p['page']} ===\n{text}")
    return "\n\n".join(lines)


def match_transcript_to_slides(
    transcript_path: str,
    pdf_json_path: str,
    output_path: str,
):
    """Use Gemini to insert slide boundaries into the transcript."""
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    client = genai.Client(api_key=api_key)

    with open(transcript_path, "r", encoding="utf-8") as f:
        transcript = f.read()

    pdf_content = load_pdf_content(pdf_json_path)

    prompt = f"""You are given two inputs:

1. **SLIDE CONTENT**: Text extracted from each of the 85 slides of an academic presentation about "Multimodal Data for Robot Manipulation: From Tactile Sensing to Scalable Human Demonstrations" by Hojung Choi.

2. **FULL TRANSCRIPT**: A verbatim transcription of the presenter speaking through these 85 slides, in order.

Your task: Insert slide boundary markers into the transcript so that each segment corresponds to the slide being discussed.

## Rules:
- Output the FULL transcript text (do not omit or summarize any words)
- Insert markers in the format: `\\n\\n--- Slide X: [slide title or brief description] ---\\n\\n` at each slide transition
- The slides go from 1 to 85 in order — the presenter never goes backwards
- Some slides may have very short or no spoken content (e.g., transition slides, title slides) — still mark them
- Use the slide text content to identify topic transitions and keyword matches
- If you're uncertain about an exact boundary, make your best guess based on topic flow
- Start with `--- Slide 1: ... ---` before the first words
- Every slide from 1 to 85 must appear exactly once

## SLIDE CONTENT:
{pdf_content}

## FULL TRANSCRIPT:
{transcript}

## OUTPUT:
Return the full transcript with slide boundary markers inserted. Nothing else."""

    print("Sending to Gemini for slide matching...")
    print(f"Transcript length: {len(transcript)} chars")
    print(f"PDF content length: {len(pdf_content)} chars")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt],
        config=genai.types.GenerateContentConfig(
            max_output_tokens=65536,
        ),
    )

    result = response.text

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)

    # Count how many slide markers were inserted
    import re
    slide_markers = re.findall(r"--- Slide (\d+)", result)
    print(f"Slide markers found: {len(slide_markers)}")
    print(f"Output saved to {output_path}")

    return result


def format_final_output(matched_path: str, qa_transcript_path: str, final_path: str):
    """Create the final formatted markdown output."""
    with open(matched_path, "r", encoding="utf-8") as f:
        matched = f.read()

    qa_text = ""
    if os.path.exists(qa_transcript_path):
        with open(qa_transcript_path, "r", encoding="utf-8") as f:
            qa_text = f.read()

    output = f"""# Presentation Script: Multimodal Data for Robot Manipulation
## By Hojung Choi — SNU Data Science Seminar 2026

---

# Main Presentation

{matched}

---

# Q&A Session

{qa_text}
"""

    with open(final_path, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"Final output saved to {final_path}")


if __name__ == "__main__":
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base, "output")

    matched = match_transcript_to_slides(
        transcript_path=os.path.join(output_dir, "main_transcript.txt"),
        pdf_json_path=os.path.join(output_dir, "pdf_pages_content.json"),
        output_path=os.path.join(output_dir, "matched_transcript.md"),
    )

    format_final_output(
        matched_path=os.path.join(output_dir, "matched_transcript.md"),
        qa_transcript_path=os.path.join(output_dir, "qa_transcript.txt"),
        final_path=os.path.join(output_dir, "slide_scripts.md"),
    )
