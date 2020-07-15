# Given a Text and a Pattern (str to search), we have to check if that Pattern
# exists in the given string using Recursive method.
def exact_match(text, pattern, text_ind, pattern_ind):
    if pattern_ind == len(pattern):
        # If we are moving till here, then we found what we want.
        return 1

    if text_ind == len(text) and pattern_ind != len(pattern):
        return 0

    if text[text_ind] == pattern[pattern_ind]:
        # we eventually reach end of the pattern if pattern exists.
        return exact_match(text, pattern, text_ind+1, pattern_ind+1)


def contains(text, pattern, text_ind, pattern_ind):
    if text_ind == len(text):
        return 0

    # if letter at present index is equal to letter at pattern_ind
    if text[text_ind] == pattern[pattern_ind]:
        # as we had first letter match, we now want to see if
        # it is the string we are searching for. By doing exact_match
        if exact_match(text, pattern, text_ind, pattern_ind):
            return 1
        else:
            print(text_ind+1, pattern_ind+1)
            return contains(text, pattern, text_ind+1, pattern_ind+1)

    # as in our example "Hello world" text and "world" pattern, starting
    # character doesn't match. We should go on till we find a match.
    return contains(text, pattern, text_ind+1, pattern_ind)


if __name__ == "__main__":
    print(contains("llo Mr Robot", "Mr Robot", 0, 0))
