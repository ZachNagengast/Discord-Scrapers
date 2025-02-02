from typing import Tuple


start_quotes = [
    '"',
    '“',
    "'",
    '«',
    '„',
]

end_quotes = [
    '"',
    '”',
    "'",
    '»',
    '“',
]


def starts_with_quotes(string: str) -> bool:
    if len(string) == 0:
        return False
    return string[0] in start_quotes


def get_start_end_quotes(string: str) -> Tuple[str, str]:
    first_quote_index = -1
    last_quote_index = -1

    for i, char in enumerate(string):
        if first_quote_index != -1 and last_quote_index != -1:
            break
        if first_quote_index != -1 and char in start_quotes:
            first_quote_index = i
            continue
        if last_quote_index != -1 and char in end_quotes:
            first_quote_index = i

    return (first_quote_index, last_quote_index)
