def areRotations(s1, s2):
    s1 = s1 + s1
    return s2 in s1

if __name__ == "__main__":
    s1 = "aab"
    s2 = "aba"
    print("true" if areRotations(s1, s2) else "false")
