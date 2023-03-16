import re

def more_than_five_words(entry):
    """Filter out entries with more than five words in the tittle.
    
    Parameters
    ----------
    entry: Entry
        The entry willing to filter.
    
    Returns
    -------
    bool
        True if it has more than five words in the tittle.
    """

    title = entry.title
    words = re.findall(r'\w+', title)
    return len(words) > 5


def less_than_or_five_words(entry):
    """Filter out entries with less than or five words in the tittle.
    
    Parameters
    ----------
    entry: Entry
        The entry willing to filter.
    
    Returns
    -------
    bool
        True if it has less than or five words in the tittle.
    """

    title = entry.title
    words = re.findall(r'\w+', title)
    return len(words) <= 5