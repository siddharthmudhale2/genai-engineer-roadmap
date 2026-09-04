from src.renderer import render_summary_prompt
from src.validator import validate_prompt


def main() -> None:
    document = """
    Python is a high-level programming language.
    It is widely used in web development, automation,
    data science, and artificial intelligence.
    """

    prompt = render_summary_prompt(document)

    validate_prompt(prompt)

    print("Generated Prompt:")
    print("=" * 60)
    print(prompt)


if __name__ == "__main__":
    main()