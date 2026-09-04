SUMMARY_PROMPT = """
You are a professional summarization assistant.

Task:
Summarize the provided document.

Requirements:
- Keep the summary concise.
- Preserve important facts.
- Do not invent information.
- Use simple language.

Document:
<document>
{document}
</document>

Output:
Return a concise paragraph.
"""