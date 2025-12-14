import os
import re
import json
from typing import List
from pydantic import BaseModel, Field
from google import genai
from google.genai import types
from ..config import gemini_api_key


class NoteSummary(BaseModel):
    summary: str = Field(description="Ringkasan 1-2 kalimat.")
    bullets: List[str] = Field(description="3-7 tags, masing-masing 1-2 kata.")


class NoteSummaryError(Exception): ...


class NoteSummaryConfigError(NoteSummaryError): ...


class NoteSummaryAPIError(NoteSummaryError): ...


class NoteSummaryParseError(NoteSummaryError): ...


class NoteAI:
    TAG_PATTERN = r"^[A-Za-z0-9]+(?:[ -][A-Za-z0-9]+)?$"

    def __init__(self, model: str = "gemini-2.5-flash"):
        api_key = gemini_api_key
        if not api_key:
            raise NoteSummaryConfigError(
                "Missing GEMINI_API_KEY / GOOGLE_API_KEY env var."
            )

        self.client = genai.Client(api_key=api_key)
        self.model = model
        self._tag_re = re.compile(self.TAG_PATTERN)

    def _to_tag(self, s: str) -> str:
        s = " ".join((s or "").strip().split()[:2])
        s = re.sub(r"[^A-Za-z0-9 -]", "", s).strip()
        return s if (s and self._tag_re.match(s)) else ""

    def _extract_json_text(self, text: str) -> str:
        if not text:
            return ""
        text = text.strip()
        text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s*```$", "", text)
        start, end = text.find("{"), text.rfind("}")
        if start != -1 and end != -1 and end > start:
            return text[start : end + 1].strip()
        return text

    def summarize_note(self, note_text: str) -> dict:
        note_text = (note_text or "").strip()
        if not note_text:
            raise ValueError("note_text is empty")

        prompt = f"""
Ringkas catatan berikut dalam Bahasa Indonesia.

Output HARUS JSON valid:
{{
  "summary": "1-2 kalimat",
  "bullets": ["tag 1-2 kata", "tag 1-2 kata", "tag 1-2 kata"]
}}

Aturan bullets/tag:
- setiap item 1–2 kata saja
- jangan pakai kalimat panjang
- contoh: "deadline", "next steps", "api", "ui"

CATATAN:
\"\"\"{note_text}\"\"\"
""".strip()

        try:
            resp = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.2,
                    max_output_tokens=400,
                    response_mime_type="application/json",
                    response_schema=NoteSummary,
                ),
            )
        except Exception as e:
            raise NoteSummaryAPIError("Failed to call Gemini API.") from e

        data = getattr(resp, "parsed", None)
        if isinstance(data, NoteSummary):
            data = data.model_dump()

        if data is None:
            try:
                data = json.loads(
                    self._extract_json_text(getattr(resp, "text", "") or "")
                )
            except json.JSONDecodeError as e:
                raise NoteSummaryParseError("Model returned non-JSON response.") from e

        if not isinstance(data, dict):
            raise NoteSummaryParseError("Parsed response is not an object/dict.")

        summary = str(data.get("summary", "")).strip()
        bullets = data.get("bullets", [])

        if not summary:
            raise NoteSummaryParseError("Missing/invalid 'summary'.")
        if not isinstance(bullets, list):
            raise NoteSummaryParseError("Missing/invalid 'bullets' (must be a list).")

        tags, seen = [], set()
        for b in bullets:
            tag = self._to_tag(str(b))
            k = tag.lower()
            if tag and k not in seen:
                seen.add(k)
                tags.append(tag)

        if len(tags) < 3:
            raise NoteSummaryParseError(
                "Could not produce enough valid tags (need at least 3)."
            )

        return {"summary": summary, "bullets": tags[:7]}
