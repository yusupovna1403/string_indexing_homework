def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s > '0' and s < '9':
        return int(s)
    else:
        return -1
print(main("4"))
print(main("k"))
