def main(list1):
    """A list of several elements is given. Return all items from the beginning in three steps.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    return list1[ : : 3]

print(main(['a', 'ss', 'f', 'g', 'fv', 4, 2, 6]))