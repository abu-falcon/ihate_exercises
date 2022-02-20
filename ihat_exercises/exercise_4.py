import re
import string

ALL_LETTERS = string.ascii_letters


def extract_SIG_letters(d: dict[str, str]) -> list[tuple[str, str]]:
    """
    extract value and key if the key matches exactly 'SIG' + (one or more letter [small/big]) + (anything else [could be empty])

    Example:

    {
        "heSIGabc": "a",
        "sigabc": "b",
        "SIGABc": "c",
        "SIGab3": "d",
        "SIBabc": "e",
        "SIGa": "f",
        "SIG": "g",
        "SIGk11111A": "h",

    }    ---> [("c", "SIGABc"), ('d', 'SIGab3'), ("f", "SIGa"), ("h","SIGk11111A")]
    """
    result: list[tuple[str, str]] = []
    for k, v in d.items():
        key_cut = [c for c in k]
        match key_cut:
            case ["S", "I", "G", let, *_] if let in ALL_LETTERS:
                result.append((v, k))
    return result
    ## Another solution
    # return [(v, k) for k, v in d.items() if re.match(r"SIG[a-zA-Z]+", k)]
