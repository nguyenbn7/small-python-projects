import re

_credit_card_pattern = re.compile(
    r"""
    ((\d{4})[-\s*]?\d{4}[-\s*]?\d{4}[-\s*]?(\d{4}))
    """,
    re.VERBOSE,
)


def mask_credit_card(card: str, show_first_4_digits=False):
    if show_first_4_digits:
        return _credit_card_pattern.sub(r"\2********\3", card)

    return _credit_card_pattern.sub(r"************\3", card)
