"""
Given a String, and a Pattern(Substring) to search in the original String.
Procedure:
1. We Start with beginning of String and matching beginning
of Pattern(Substring). i.e., 0th index <--> 0th index
2. If this matches, we start doing exact match for remaining string followed.
3. We return 1, if we looped till end of Pattern(Substring).
4. We return 0, if we didn't find exact string that's in Pattern which isn't in
String, while looping.
5. So, we now move to second index and start matching this index with Pattern
index.
i.e, 1st <---> 1st Index. If matched, we start doing Exact match from here.
"""


def exact_match(text, pattern, text_ind, pattern_ind):
    if pattern_ind == len(pattern):
        return 1

    if text_ind == len(text) and pattern_ind != len(pattern):
        return 0

    if text[text_ind] == pattern[pattern_ind]:
        return exact_match(text, pattern, text_ind+1, pattern_ind+1)


def contains(text, pattern, text_ind, pattern_ind):
    if text[text_ind] == pattern[pattern_ind]:
        if exact_match(text, pattern, text_ind, pattern_ind):
            return 1
        else:
            return contains(text, pattern, text_ind+1, pattern_ind+1)

    return contains(text, pattern, text_ind+1, pattern_ind)


if __name__ == "__main__":
    print(contains("Hello Friend, this is MR.Robot", "lajsls", 0, 0))
