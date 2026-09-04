def validate_prompt(prompt: str) -> None:
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    required_sections = [
        "Task:",
        "Requirements:",
        "<document>",
        "</document>",
    ]

    for section in required_sections:
        if section not in prompt:
            raise ValueError(
                f"Missing required section: {section}"
            )