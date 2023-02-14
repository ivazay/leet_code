"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving
the order of characters. No two characters may map to the same character, but a character may map to itself.

Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""


def transform_string(string: str) -> str:
    letters = {}
    new_str = []

    for i, char in enumerate(string):
        if char not in letters:
            letters[char] = i
        new_str.append(str(letters[char]))

    return " ".join(new_str)


def is_isomorphic(s: str, t: str) -> bool:
    return transform_string(s) == transform_string(t)


if __name__ == '__main__':
    assert is_isomorphic("egg", "add") is True
    assert is_isomorphic("foo", "bar") is False
    assert is_isomorphic("paper", "title") is True
    assert is_isomorphic("badc", "baba") is False
    assert is_isomorphic("egcd", "adfd") is False
    assert is_isomorphic("abcdefghijklmnopqrstuvwxyzva", "abcdefghijklmnopqrstuvwxyzck") is False
    assert is_isomorphic("aaaaabbbbbcccccdddddeeeee", "pppppqqqqqrrrrrsssssttttt") is True
