from src.prompts import SUMMARY_PROMPT


def render_summary_prompt(document: str) -> str:
    if not document.strip():
        raise ValueError("Document cannot be empty.")

    return SUMMARY_PROMPT.format(document=document)