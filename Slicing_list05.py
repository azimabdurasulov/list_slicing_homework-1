def main(list1,n,k):
    """
    A list of several elements is given. Return the value from n index to k index.
    Args:
        list1(list): parameter
        n(int): parameter
        k(int): parameter
    Returns:
        list: return answer.
    """
    return list1[ n:k + 1 ]

print(main(['s', 'e', 's', 3, 4, 11, 8, 9], 2, 6))