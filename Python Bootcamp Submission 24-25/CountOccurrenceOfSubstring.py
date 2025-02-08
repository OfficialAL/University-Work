def countFreq(pat, txt):
    M = len(pat)
    N = len(txt)
    res = 0
 
    # A loop to slide pat[] one by one
    for i in range(N - M + 1):
 
        # For current index i, check
        # for pattern match
        j = 0
        while j < M:
            if (txt[i + j] != pat[j]):
                break
            j += 1
 
        if (j == M):
            res += 1
            j = 0
    return res
 

if __name__ == 'main':
    txt = "heymanman"
    pat = "man"
    print(countFreq(pat, txt))
