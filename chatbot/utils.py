def count_tokens(s: str) -> int:
    """
    TODO: Use a tokenizer
    """
    if not s:
        return 0
    return len(tuple(t for t in s.split() if t))
