def main(s):
    """
    The s string variable is given. Return three characters from the beginning.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    ans = ''
    ans = s[0] + s[1] + s[2]
    return ans
a = "python"
print(a[0:3])
print(main("code"))
