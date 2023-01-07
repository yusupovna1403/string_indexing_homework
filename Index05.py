def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    sum = 0
    idx = 0
    if s[idx] >= '0' and s[idx] <= '9':
        sum+=1
    idx+=1
    if s[idx] >= '0' and s[idx] <= '9':
        sum+=1
    idx+=1
    if s[idx] >= '0' and s[idx] <= '9':
        sum+=1
    idx+=1
    if s[idx] >= '0' and s[idx] <= '9':
        sum+=1
    idx+=1
    if s[idx] >= '0' and s[idx] <= '9':
        sum+=1
    idx+=1
    return sum
    
print(main("a1b23c"))
