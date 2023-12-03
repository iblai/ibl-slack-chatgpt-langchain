import tiktoken


def count_tokens(text: str) -> int:
    """
    Encodes and returns the token count for a given string.

    Params:
        text (str): A given string to be encoded by a tokenizer.
    Dependencies:
        tiktoken (Encoder): BPE tokenizer for use with OpenAI's models.
    """

    if text is None or text.strip() == "":
        return 0

    tokenizer = tiktoken.encoding_for_model("gpt-4")
    tokenized_text = tokenizer.encode(text)
    return len(tokenized_text)
