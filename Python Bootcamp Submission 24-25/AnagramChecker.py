def anagrams(inp1: str, inp2: str) -> bool:
    if len(inp1) != len(inp2):
        return False

    counts = {}

    for c1, c2 in zip(inp1, inp2):
        if c1 in counts.keys():
            counts[c1] += 1
        else:
            counts[c1] = 1
        if c2 in counts.keys():
            counts[c2] -= 1
        else:
            counts[c2] = -1

    for count in counts.values():
        if count != 0:
            return False
    return True

def main():
    inp1 = "listen"
    inp2 = "silent"
    if anagrams(inp1, inp2):
        print(f"{inp1} and {inp2} are anagrams")
    else:
        print(f"{inp1} and {inp2} are not anagrams")

if __name__ == "__main__":
    main()
