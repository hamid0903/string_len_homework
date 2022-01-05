def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    a=len(s1)%2
    b=len(s2)%2
    c=len(s3)%2
    ans=""
    x1="["
    x2="]"
    if a!=1:
        ans=x1+s2+s3+x2
    if b!=1:
        ans=x1+s1+s3+x2
    if c!=1:
        ans=x1+s1+s2+x2
    else:
        x1+x2

    return ans
print(main("ab", "abc", "abcd"))