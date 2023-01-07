def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    
    idx = 0
    if s[idx] == "*":
        return idx
    idx+=1
    if s[idx] == "*":
        return idx
    idx+=1
    if s[idx] == "*":
        return idx
    idx+=1
    if s[idx] == "*":
        return idx
    else:
        return False
    
print(main("c*e"))
print(main("good"))

        