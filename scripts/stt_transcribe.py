#!/usr/bin/env python3
"""Transcribe audio files using Gemini API."""

import os
import sys
import time
from google import genai

def transcribe_audio(audio_path: str, output_path: str, section_label: str):
    """Upload audio to Gemini and get verbatim transcription."""
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: No GEMINI_API_KEY or GOOGLE_API_KEY found")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    print(f"[{section_label}] Uploading {audio_path}...")
    audio_file = client.files.upload(file=audio_path)

    # Wait for file to be processed
    while audio_file.state.name == "PROCESSING":
        print(f"[{section_label}] Waiting for file processing...")
        time.sleep(5)
        audio_file = client.files.get(name=audio_file.name)

    if audio_file.state.name == "FAILED":
        print(f"[{section_label}] File processing failed!")
        sys.exit(1)

    print(f"[{section_label}] File ready. Requesting transcription...")

    prompt = """Transcribe this audio verbatim. This is an academic presentation about robot manipulation and tactile sensing.

Rules:
- Transcribe every word spoken, exactly as said
- Include filler words (um, uh, so, etc.) only if they are significant
- Use proper punctuation and paragraph breaks for readability
- When the speaker references a slide or figure, note it naturally as spoken
- Do NOT add timestamps
- Do NOT add speaker labels unless multiple speakers are clearly distinguishable
- Output plain text only"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[audio_file, prompt],
    )

    transcript = response.text

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(transcript)

    print(f"[{section_label}] Transcription saved to {output_path}")
    print(f"[{section_label}] Length: {len(transcript)} characters")

    # Clean up uploaded file
    try:
        client.files.delete(name=audio_file.name)
    except Exception:
        pass

    return transcript


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: stt_transcribe.py <audio_path> <output_path> <label>")
        sys.exit(1)

    transcribe_audio(sys.argv[1], sys.argv[2], sys.argv[3])
