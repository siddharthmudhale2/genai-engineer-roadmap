SUMMARY_PROMPT = """
You are a professional summarization assistant.

Summarize the following document.

Requirements:
- Preserve important facts.
- Do not invent information.
- Use simple language.
- Keep the answer concise.

<document>
{document}
</document>
"""


def build_summary_prompt(document: str) -> str:
    if not document.strip():
        raise ValueError("Document cannot be empty.")

    return SUMMARY_PROMPT.format(document=document)