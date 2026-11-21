###
# Module with functions operating on text
#


def word_count(text):
    """Returns the number of words in the text."""
    return len(text.split())


def words_by_length(text):
    """Returns words ordered from the longest to the shortest."""
    return sorted(text.split(), key=len, reverse=True)


def words_alphabetically(text):
    """Returns words in alphabetical order (ignoring letter case)."""
    return sorted(text.split(), key=str.lower)
