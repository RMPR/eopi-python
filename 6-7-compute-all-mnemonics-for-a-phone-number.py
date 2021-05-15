"""
Write a program which takes as input a phone number, specified as a string of digits, and returns
all possible character sequences that correspond to the phone number. The cell phone keypad is
specified by a mapping that takes a digit and returns the corresponding set of characters. The
character sequences do not have to be legal words or phrases.
"""

KEYPAD: dict = {"2": "ABC", "3": "DEF", "4": "GHI", "5": "JKL", "6": "MNO",
                "7": "PQRS", "8": "TUV", "9": "WXYZ"}


def character_sequences(digits: str):
    result: set = set()
    n: int = len(digits)

    def build_words(word: str, pos: int):
        if pos == n:
            result.add("".join(word))
        else:
            for letter in KEYPAD.get(digits[pos], ""):
                build_words(word + letter, pos + 1)
    if not digits:
        return set()

    build_words("", 0)
    return result


if __name__ == "__main__":
    assert(character_sequences("23") == {
           "AD", "AE", "AF", "BD", "BE", "BF", "CD", "CE", "CF"})
    assert(character_sequences("7") == {"P", "Q", "R", "S"})
    assert(character_sequences("0") == set())
    assert(character_sequences("") == set())
