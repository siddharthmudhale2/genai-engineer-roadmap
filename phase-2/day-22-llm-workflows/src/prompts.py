EXTRACTION_PROMPT = """
Extract candidate information from the text below.

Return JSON with:
{{
    "name": "string",
    "experience_years": 0,
    "skills": ["string"]
}}

Candidate:
<candidate>
{candidate_text}
</candidate>
"""


RECOMMENDATION_PROMPT = """
You are a recruitment assistant.

Based on the job matching result below, provide a recommendation.

Return JSON:

{{
    "decision": "string",
    "reason": "string"
}}

Match:
<match>
{match}
</match>
"""