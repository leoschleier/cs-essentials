
def is_unique(s: str) -> bool:
    s_len = len(s)
    for i in range(s_len):
        s_i = s[i]
        for ii in range(i+1, s_len):
            if s_i == s[ii]:
                return False

    return True
        

if __name__ == "__main__":
    print(is_unique("Unique str."))
    print(is_unique("Not unique str."))

