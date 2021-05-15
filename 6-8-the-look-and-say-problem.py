"""
The look-and-say sequence starts with 1. Subsequent numbers are derived by describing the
previous number in terms of consecutive digits. Specifically, to generate an entry of the sequence
from the previous entry, read off the digits of the previous entry, counting the number of digits in
grouPs of the same digit. For example, 1; one 1; two 1s; one 2 then one 1; one 1, then one 2, then
two 1s; three 1s, then two 2s, then one 1. The first eight numbers in the look-and-say sequence are
<'t,
1.1.,
21, 1211, 111221, 31221.1., 13112227, 1113213211>
Write a Program that takes as input an integer
sequence. Retum the result as a string.
"""


def look_and_say(n: int):
    if n < 1:
        return ""

    def look_and_say_helper(entry: list, step: int):
        new_entry: list = []
        last_seen: int = entry[0]
        number: int = 0
        if step == n:
            return "".join(entry)
        for i in range(len(entry)):
            if entry[i] != last_seen and i < len(entry):
                new_entry.extend([str(number), last_seen])
                last_seen = entry[i]
                number = 1
            else:
                number += 1
        #  Don't forget the last_seen one
        new_entry.extend([str(number), entry[-1]])
        return look_and_say_helper(new_entry, step + 1)

    result = look_and_say_helper(entry=["1"], step=1)
    return result


if __name__ == "__main__":
    assert(look_and_say(1) == "1")
    assert(look_and_say(2) == "11")
    assert(look_and_say(3) == "21")
    assert(look_and_say(4) == "1211")
    assert(look_and_say(5) == "111221")
    assert(look_and_say(6) == "312211")
    assert(look_and_say(7) == "13112221")
    assert(look_and_say(8) == "1113213211")
    assert(look_and_say(0) == "")
    assert(look_and_say(-1) == "")
