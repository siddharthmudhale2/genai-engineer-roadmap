CANDIDATE_ANALYSIS_PROMPT = """
You are an AI recruitment assistant.

Analyze the candidate information below.

Return a JSON object with exactly these fields:

{{
    "name": "string",
    "experience_years": 0,
    "skills": ["string"],
    "suitable": true
}}

Rules:
- experience_years must be a non-negative integer.
- skills must be an array of strings.
- suitable must be true or false.
- Do not add additional fields.
- Do not include markdown code fences.

Candidate information:
<candidate>
{candidate_text}
</candidate>
"""


def build_candidate_prompt(candidate_text: str) -> str:
    if not candidate_text.strip():
        raise ValueError("Candidate information cannot be empty.")

    return CANDIDATE_ANALYSIS_PROMPT.format(
        candidate_text=candidate_text
    )