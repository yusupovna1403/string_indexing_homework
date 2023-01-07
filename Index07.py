def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    if len(s) > n:
        return s[n]
    else:
        return False
print(main("code",4))
print(main("python",3))
