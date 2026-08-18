def clean_text(text):
    return " ".join(text.strip().split())


def count_words(text):
    return len(text.split())