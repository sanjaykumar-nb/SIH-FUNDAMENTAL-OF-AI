BAD_WORDS = {"damn", "hell", "shit", "fuck", "asshole"}  # Sample list

def filter_bad_language(message: str) -> str:
    words = message.lower().split()
    filtered_words = [word if word not in BAD_WORDS else "[FILTERED]" for word in words]
    return " ".join(filtered_words)
